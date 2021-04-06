from django.urls import path, include
from Users import views

urlpatterns = [
    path('accounts/', include("django.contrib.auth.urls")),
    path('register/', views.register_page, name='register'),
]