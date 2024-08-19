from django.shortcuts import render, redirect
from django.contrib.auth import logout 

def home(request):
    user = request.user
    context = {
        'email': user.email,
        'username': user.username,
        'password': user.password,
    }
    print(context)
    return render(request, 'home.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')