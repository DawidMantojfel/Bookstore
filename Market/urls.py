from django.urls import path
from Market.views import home, BookDetailView, book_search, add_to_cart, basket,delete_from_cart


urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', BookDetailView.as_view(), name='product_detail'),
    path('search/', book_search, name='book_search'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('basket/', basket, name='basket'),
    path('delete_from_cart/<int:id>', delete_from_cart, name='delete_from_cart'),
    ]
