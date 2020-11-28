from django.shortcuts import render
from django.contrib.auth import authenticate #con este se busca en la DB
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
#from django.contrib.auth.models import user

from .forms import RegisterForm

def index(request):

    return render(request, 'index.html', {    })

def seguimiento(request):
    return render(request, 'seguimiento.html', {    })

def dof(request):
    return render(request, 'dof.html', {    })

def inegi(request):
    return render(request, 'inegi.html', {    })

def shcp(request):
    return render(request, 'shcp.html', {    })

def prof(request):
    return render(request, 'profesionistas.html', {    })

def ong(request):
    return render(request, 'ong.html', {    })

def gob(request):
    return render(request, 'gobierno.html', {    })

def gral(request):
    return render(request, 'general.html', {    })

def pagos(request):
    return render(request, 'pagos.html', {    })

def nos(request):
    return render(request, 'nosotros.html', {    })

def faq(request):
    return render(request, 'faq.html', {    })    

def contacto(request):
    return render(request, 'contacto.html', {    })

def terms(request):
    return render(request, 'terminos.html', {    })

def privacy(request):
    return render(request, 'privacidad.html', {    })

def detalle(request):
    return render(request, 'detalle.html', {    })


"""
def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password) 
        #authenticate devuelve objeto user, si no existe devuelve none
        if user:
            login(request,user)
            messages.success(request,'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña no válidos')
    #else:
    #    return render(request,'empty.html', { })
    return render(request,'login.html', { })
"""


"""
def logoutView(request):
    logout(request)
    messages.success(request, 'Sesión cerrada')
    return redirect('login')
"""

def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        nombre= form.cleaned_data.get('username') #cleaned_date trae un diccionario
        aPaterno = form.cleaned_data.get('aPaterno')
        aMaterno = form.cleaned_data.get('aMaterno')
        email = form.cleaned_data.get('email')
        telefono = form.cleaned_data.get('telefono')
        password = form.cleaned_data.get('password')

        print(nombre)
        print(email)
        print(password)

    return render(request, 'registro.html', {
        'form' : form
    })

"""
def micuenta(request):
    return render(request, 'micuenta.html', {})
"""
