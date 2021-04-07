from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import CreateUserForm
from django.contrib import messages
from Market.views import home


def register_page(request):
    form = CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'Users/register.html', context)


# def login_page(request):
#     context = {}
#
#     return render(request, 'Users/login.html', context)