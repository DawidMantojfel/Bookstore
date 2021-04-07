import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.renderers import JSONRenderer
from bookstore.settings import BASE_DIR
from .models import Product, Order, OrderItem
from .forms import BookModel as Book
from .forms import BookOffer
from django.views.generic.detail import DetailView
import requests
from django.http import JsonResponse
import json
from Market.api.serializers import ProductSerializer


def home(request):
    context = {}
    products = Product.objects.all()
    context['products'] = products

    if request.method == "POST":
        data = json.loads(request.body)
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
                messages.add_message(request,messages.INFO, 'Item was Added !')
            else:
                messages.add_message(request, messages.ERROR, 'There is not that much product !')
        orderItem.save()
        context['messages'] = messages

    return render(request, 'market/home.html', context)


def add_to_cart(request):
    data = json.loads(request.body)
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
            messages.add_message(request, messages.ERROR ,'There is not that much product !')
    orderItem.save()

    return JsonResponse('item was added', safe=False)

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


def basket(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        # order and items are the same for now
        items = order.orderitem_set.all()
        # products = OrderItem.objects.filter(product__user=customer)

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    # now its rendering products of customer
    context = {'items': items, 'order': order}
    return render(request, 'market/basket.html', context)


class DisplayJsonBooks:
    BASE_URL = 'https://www.googleapis.com/books/v1/volumes?q={}&printType=books&maxResults=40'
    FILE_NAME = 'json_books.json'

    def search_books(self, request):
        context = {}
        if request.method == "GET":
            form = BookOffer()
            search = request.GET.get('search')
            url = self.BASE_URL.format(search)
            response = requests.request('GET', url=url)
            self.write_books_to_json_file(response.json())

        elif request.method == "POST":
            data = request.POST
            user = request.user
            book_info = json.loads(data['book_values'])
            description = book_info.get('description')
            image = book_info.get('image')
            infolink = book_info.get('infolink')
            form = BookOffer(request.POST)
            if form.is_valid():
                product = form.save(commit=False)
                product.user = user
                product.infolink = infolink
                product.description = description
                product.image = image
                product.save()
                return redirect('home')

        with open((os.path.join(BASE_DIR, self.FILE_NAME)), 'r') as f:
            books = json.loads(f.read())
            context['books'] = books
        context['form'] = form

        return render(request, "market/search.html", context)

    def write_books_to_json_file(self, response):
        static_image_url = "/static/images/default.jpg"
        books = {"books":[]}
        book = {}
        for result in response['items']:
            book['title'] = result['volumeInfo'].get('title')
            authors = result['volumeInfo'].get('authors')
            book['authors'] = ", ".join(authors) if authors else authors
            book['infolink'] = result['volumeInfo'].get('infoLink')
            image = result['volumeInfo'].get('imageLinks')
            book['image'] = image.get('smallThumbnail') if image else static_image_url
            book['description'] = result['volumeInfo'].get('description')
            books['books'].append(book)
            book = {}

        with open((os.path.join(BASE_DIR, self.FILE_NAME)), 'w') as f:
            f.write(json.dumps(books, indent=4))

def advanced_search(reqeust):
    return render(reqeust,'market/advanced_search.html' )




