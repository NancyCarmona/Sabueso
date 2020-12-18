from django.shortcuts import render
from django.contrib.auth import authenticate #con este se busca en la DB
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import RegisterForm
from .forms import LoginForm

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



def loginView(request):
    formLogin = LoginForm(request.POST or None)
    if request.method == 'POST'and formLogin.is_valid():
        email = formLogin.cleaned_data.get('e_mail')
        password = formLogin.cleaned_data.get('password')
        user = authenticate(username=email, password=password) 
        #authenticate devuelve objeto user, si no existe devuelve none
        if user:
            login(request,user)
            #messages.success(request,'Bienvenida/o {}'.format(user.first_name))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña no válidos')
    #else:
    #    return render(request,'empty.html', { })
    return render(request,'login.html', {
        'formLogin': formLogin,
     })




def logoutView(request):
    logout(request)
    #messages.success(request, 'Sesión cerrada')
    return redirect('login')


def register(request):
    formRegistro = RegisterForm(request.POST or None)#llenarlo con los datos o crearlo vacío
    
    if request.method == 'POST' and formRegistro.is_valid():
        user = formRegistro.save()
        if user:
            login(request, user)
            messages.success(request, "Usuario creado. Inicie sesión con su correo electrónico")
            return redirect('index')

    return render(request, 'registro.html', {
        'formRegistro' : formRegistro, # 'nombreForm': objeto
    })

"""
def micuenta(request):
    return render(request, 'micuenta.html', {})
"""

"""    
esto iba en el if
            apellidos = formRegistro.cleaned_data.get('apellidos')
            company = formRegistro.cleaned_data.get('compania')
            email = formRegistro.cleaned_data.get('email')
            telefono = formRegistro.cleaned_data.get('telefono')
            direccion = formRegistro.cleaned_data.get('direccion')
            colonia = formRegistro.cleaned_data.get('colonia')
            ciudad = formRegistro.cleaned_data.get('telefono')
            estado = formRegistro.cleaned_data.get('estado')
            codigopostal = formRegistro.cleaned_data.get('codigopostal')
            password = formRegistro.cleaned_data.get('password')

            print(nombre)
            print(email)
            print(password)
        """
        #if request.POST.get('login_flotante'):
        #if request.method == 'POST' and formLogin.is_valid():