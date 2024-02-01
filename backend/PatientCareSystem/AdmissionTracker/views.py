from django.shortcuts import render
from .models import *
from .views import *
# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST[password]
        print(f"username is {username}")
        print(f"password is {password}")