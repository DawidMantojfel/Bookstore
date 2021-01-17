from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Book, Market
from .forms import BookOffer
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
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
    results = []
    context = {}
    if request.method == 'GET':
        api_key = 'AIzaSyAZ3oOt4i0cX6i8Uc2Fn1I2NlLM4AZQA1Y'
        user_query = request.GET.get('search')
        url = f'https://www.googleapis.com/books/v1/volumes?q={user_query}'
        response_title = requests.request('GET', url).json()
        print(response_title)
        for result in response_title['items']:
            results.append(result['volumeInfo']['title'])
            results.append(result['volumeInfo']['authors'])
        context['books'] = results




    # response = requests.request("POST", url)

    return render(request, "market/search.html", context)


def book_add(request):
    if request.method == "POST":
        form = BookOffer(request.POST)
        if form.is_valid():
            form.save()
    form = BookOffer()
    context = {'form': form}
    return render(request, 'market/add_book.html', context)
