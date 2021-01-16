from django.urls import path
from Market.views import BooksListView, BookDetailView, book_search


urlpatterns = [
    path('', BooksListView.as_view(), name='home'),
    path('<int:pk>/', BookDetailView.as_view(), name='market_detail'),
    path('search/', book_search, name='book_search')
]