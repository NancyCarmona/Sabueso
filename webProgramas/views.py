from django.shortcuts import render
from django.contrib.auth import authenticate #con este se busca en la DB
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib import messages

def index(request):
    return render(request, 'index.html', {    })

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password) #devuelve user, si no devuelve none
        if user:
            login(request,user)
            print('si jaló we')
            messages.success(request,'Bienvenido'.format(user.username))
            return redirect('index')
        else:
            print('no jaló we')
            messages.error(request, 'Usuario o contraseña no válidos')
    return render(request,'login.html', {    })

def vacia(request):
    print('no c k pasa')
    return render(request, 'empty.html')