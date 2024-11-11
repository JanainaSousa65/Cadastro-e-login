# auth_app/urls.py
from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('sair', views.sair, name='sair'),
]
#urlpatterns += [
#    path('login/', auth_views.LoginView.as_view(template_name='auth_app/login.html'), name='login'),
#]