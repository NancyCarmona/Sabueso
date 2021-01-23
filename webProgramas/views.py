from django.shortcuts import render
from django.contrib.auth import authenticate #con este se busca en la DB
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import date

from .forms import RegisterForm
from .forms import LoginForm
from .forms import ConsultaFechaForm
from users.models import DescargaNotaDOF

def index(request):
    return render(request, 'index.html', {    })

def seguimiento(request):
    return render(request, 'seguimiento.html', {    })

def dof(request):
    fechaActual1='{}-{}-{}'.format(date.today().year,date.today().month,date.today().day)
    notasPorFecha = DescargaNotaDOF.objects.filter(fecha=fechaActual1)
    formConsultaFecha = ConsultaFechaForm(request.POST or None)
    if request.method == 'POST'and formConsultaFecha.is_valid():
        fechaInput = formConsultaFecha.cleaned_data.get('fecha')
        fechaBusqueda='{}-{}-{}'.format(fechaInput.year,fechaInput.month,fechaInput.day)
        notasPorFecha=DescargaNotaDOF.objects.filter(fecha=fechaBusqueda)

    return render(request, 'dof.html', { 
        'notasDOF': notasPorFecha,
        'formConsultaFecha': formConsultaFecha
       })

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

def alerta(request):
    return render(request, 'alerta.html', {    })



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

