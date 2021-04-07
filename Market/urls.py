from django.urls import path, include
from Market.api.views import ProductViewSet, UserViewSet
from Market.views import home, basket, delete_from_cart, DisplayJsonBooks, advanced_search
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'users', UserViewSet, basename='user')


urlpatterns = [
    path('', home, name='home'),
    path('search/', DisplayJsonBooks().search_books, name='book_search'),
    path('advanced_search/',advanced_search, name='advanced_search'),
    path('basket/', basket, name='basket'),
    path('delete_from_cart/<int:id>', delete_from_cart, name='delete_from_cart'),
    path('api/', include(router.urls))
    ]
