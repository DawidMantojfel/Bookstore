from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Book, Market
from .forms import BookOffer
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
import requests



# generic view
class BooksListView(ListView):
    model = Market
    ''' Fajnie by było żeby użytkownik mógł zmieniać ilość elementów wyswietlenia na stronie (default = 25)
    w generic view jest to dosc latwe bo do context django przekazuje obiekt Paginator który mozna modyfikowac '''
    paginate_by = 25
    ordering = '-date'
    context_object_name = 'market'


# function base view
# def display_books(request):
#     books = Market.objects.order_by('-date')
#     context = {'books': books}
#     print(books)
#     return render(request, "market/market_list.html", context)


class BookDetailView(DetailView):
    model = Market
    template_name = 'market/market_detail.html'
    context_object_name = 'market'


def book_search(request):
    books = []
    context = {}

    class Book:
        def __init__(self, authors, title, image=None):
            self.authors = authors
            self.title = title
            self.image = image

        def __str__(self):
            return f'{self.title} by  {self.authors}'

    if request.method == 'GET':
        api_key = 'AIzaSyAZ3oOt4i0cX6i8Uc2Fn1I2NlLM4AZQA1Y'
        user_query = request.GET.get('search')
        url = f'https://www.googleapis.com/books/v1/volumes?q={user_query}&maxResults=40'
        response = requests.request('GET', url).json()
        for result in response['items']:
            title = result['volumeInfo'].get('title')
            authors = result['volumeInfo'].get('authors')
            image = result['volumeInfo'].get('imageLinks')
            image_link = image.get('smallThumbnail', None) if image else None
            book = Book(authors=" ".join(authors) if authors else authors, title=title, image=image_link)
            books.append(book)
    p = Paginator(books, per_page=25)
    page = p.get_page(1)

    context = {
        'books': books,
        'page': page,
        'count': p.count
    }

    return render(request, "market/search.html", context)


def book_add(request):
    if request.method == "POST":
        form = BookOffer(request.POST)
        if form.is_valid():
            form.save()
    form = BookOffer()
    context = {'form': form}
    return render(request, 'market/add_book.html', context)
