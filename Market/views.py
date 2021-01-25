from django.shortcuts import render, redirect
from .models import Product
from .forms import BookOffer
from django.views.generic.detail import DetailView
import requests


def home(request):
    products = Product.objects.filter(sold=False)
    context = {'books': products}
    return render(request, 'market/home.html', context)


class BookDetailView(DetailView):
    model = Product
    template_name = 'market/market_detail.html'
    context_object_name = 'market'


books = []


def book_search(request):
    context = {}
    form = BookOffer()
    class Book:
        def __init__(self,id, authors, title, description, image=None):
            self.id = id
            self.authors = authors
            self.title = title
            self.image = image
            self.description = description

        def __str__(self):
            return f'{self.image}'

    if request.method == 'GET':
        books = []
        user_query = request.GET.get('search')
        url = f'https://www.googleapis.com/books/v1/volumes?q={user_query}&printType=books&maxResults=40'
        response = requests.request('GET', url).json()
        id = 0
        for result in response['items']:
            id += 1
            title = result['volumeInfo'].get('title')
            authors = result['volumeInfo'].get('authors')
            image = result['volumeInfo'].get('imageLinks')
            image_link = image.get('smallThumbnail') if image else "/static/images/default.jpg"
            description = result['volumeInfo'].get('description')
            book = Book(id=id, authors=" ".join(authors) if authors else authors,
                        title=title,
                        image=image_link,
                        description=description)
            books.append(book)

    elif request.method == 'POST':
        user = request.user
        form = BookOffer(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = user
            product.save()
            return redirect('home')

    context = {
        'books': books,
        'count': len(books),
        'form': form,
    }

    return render(request, "market/search.html", context)


def book_add(request):
    if request.method == "POST":
        user = request.user
        form = BookOffer(data=request.POST, files=request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = user
            product.save()
            return redirect('home')

    form = BookOffer()
    context = {'form': form}
    return render(request, 'market/add_book.html', context)


def buy_book(request):
    pass


def test(request):
    return render(request, 'market/testing.html')
