"""webProgramas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views #importa el archivo views.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'), #index duh (path, funcion, alias)
    path('login', views.loginView, name='login'), #login usuarios checar la extensión
    path('logout', views.logoutView, name='logout'), #login usuarios checar la extensión
    path('registro', views.register, name='register'),
    path('seguimiento', views.seguimiento, name='seguimiento'),
    path('dof', views.dof, name='dof'),
    path('inegi', views.inegi, name='inegi'),
    path('shcp', views.shcp, name='shcp'),
    path('profesionistas', views.prof, name='prof'),
    path('ong', views.ong, name='ong'),
    path('gobierno', views.gob, name='gob'),
    path('general', views.gral, name='gral'),
    path('pagos', views.pagos, name='pagos'),
    path('nosotros', views.nos, name='nos'),
    path('faq', views.faq, name='faq'),
    path('contacto', views.contacto, name='contacto'),
    path('terminos', views.terms, name='terms'),
    path('privacidad', views.privacy, name='privacy'),
    path('detalle', views.detalle, name='detalle'),
    #path('micuenta', views.micuenta, name='micuenta'),
    path('admin/', admin.site.urls), #esta estaba por default
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)