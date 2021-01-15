from django.urls import path
from Market.views import BooksListView, BookDetailView


urlpatterns = [
    path('', BooksListView.as_view(), name='home'),
    path('<int:pk>/', BookDetailView.as_view(), name='market_detail'),
]