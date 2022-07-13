"""EVALUACION_3_PW URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path
from . import views 
from .views import eliminarProducto,carritodecompras,agregarUsuario


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio, name="inicio"),
    path('login/',views.login, name="login"),
    path('user_admin/',views.user_admin, name="user_admin"),
    path('usuario_registrado/',views.usuario_registrado, name="usuario_registrado"),
    path('carritodecompras/', views.carritodecompras, name="carritodecompras"),
    path('contacto/',views.contacto, name="contacto"),
    path('formulario/', views.formulario, name="formulario"),
    path('productos/',views.productos, name="productos"),
    path('seguimiento/', views.seguimiento, name="seguimiento"),
    path('eliminarProducto/<id>/',views.eliminarProducto),
    path('eliminarProducto_usuario_registrado/<id>/',views.eliminarProducto_usuario_registrado),
    path('agregarProducto/', views.agregarProducto),
    path('agregarProducto2/', views.agregarProducto2),
    path('agregarProducto3/', views.agregarProducto3),
    path('agregarProducto4/', views.agregarProducto4),
    path('agregarProducto5/', views.agregarProducto5),
    path('agregarProducto6/', views.agregarProducto6),
    path('agregarUsuario/', agregarUsuario, name="agregarUsuario"),
            
]


