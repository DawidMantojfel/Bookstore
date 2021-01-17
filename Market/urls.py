from django.urls import path
from Market.views import BooksListView, BookDetailView, book_search, book_add


urlpatterns = [
    path('', BooksListView.as_view(), name='home'),
    path('<int:pk>/', BookDetailView.as_view(), name='market_detail'),
    path('search/', book_search, name='book_search'),
    path('add/', book_add, name='book_add'),
]