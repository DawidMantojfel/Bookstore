from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import BookOffer
from django.views.generic.detail import DetailView
import requests
from django.http import JsonResponse
import json


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'market/home.html', context)


def delete_from_cart(request, id):
    user = request.user
    product = Product.objects.get(id=id)
    order, created = Order.objects.get_or_create(customer=user, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if orderItem.quantity <= 1:
        orderItem.delete()
    if orderItem.quantity > 1:
        orderItem.quantity -= 1
        orderItem.save()
    print(orderItem.quantity)
    return redirect('basket')


def add_to_cart(request):
    data = json.loads(request.body)
    print(data)
    productId = data['productId']
    action = data['action']
    print('action:', action, 'productId:', productId)
    user = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=user, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    # if there is more or equal products than you want to order

    if action == "add":
        if product.quantity > orderItem.quantity:
            orderItem.quantity += 1
            messages.info(request,'Item was Added !')
        else:
            messages.error(request, 'There is not that much product !')
    orderItem.save()

    return JsonResponse('item was added', safe=False)


def basket(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        print(order)
        # order and items are the same for now
        items = order.orderitem_set.all()
        # products = OrderItem.objects.filter(product__user=customer)

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    # now its rendering products of customer
    context = {'items': items, 'order': order}
    return render(request, 'market/basket.html', context)


class BookDetailView(DetailView):
    model = Product
    template_name = 'market/product_detail.html'
    context_object_name = 'product'


books = []


def book_search(request):
    context = {}
    form = BookOffer()
    books = []

    class Book:
        def __init__(self, id, authors, title, description, image=None):
            self.id = id
            self.authors = authors
            self.title = title
            self.image = image
            self.description = description

        def __str__(self):
            return f'{self.image}'

    if request.method == 'GET':

        user_query = request.GET.get('search')
        url = f'https://www.googleapis.com/books/v1/volumes?q={user_query}&printType=books&maxResults=40'
        response = requests.request('GET', url).json()
        id = 0
        # if there is at least 1 book found
        if response['totalItems']:
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
        else:
            messages.warning(request, f'THERE IS NO BOOK WITH NAME "{user_query}"')
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


def test(request):
    return render(request, 'market/testing.html')
