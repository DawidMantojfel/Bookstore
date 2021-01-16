from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Market, Book
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


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
    search_query = request.GET.get('search')
    books = Book.objects.filer(title_icontains=search_query)
    print(books)
    return render(request, "market/search.html")
