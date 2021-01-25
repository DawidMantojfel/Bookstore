from django.urls import path
from Market.views import home, BookDetailView, book_search, book_add


urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', BookDetailView.as_view(), name='market_detail'),
    path('search/', book_search, name='book_search'),
    path('add/<int:id>', book_add, name='book_add'),
]
