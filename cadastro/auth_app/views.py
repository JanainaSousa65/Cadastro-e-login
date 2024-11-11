from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout

def sair(request):
    logout(request)
    return redirect(login)

def home(request):
    if request.method == "POST":
        usuario = request.POST.get('nome')
        senha = request.POST.get('senha')

        # Autentica o usuário
        usu = authenticate(username=usuario, password=senha)

        if usu is not None:
            # Login do usuário
            login(request, usu)

            return render(request, 'auth_app/login.html', {'msg': "Autenticado"}) 
        else:
            return render(request, 'auth_app/login.html', {'msg': "E-mail ou senha inválidos!"})
    return render(request, 'auth_app/login.html',  {'msg': ''})

def cadastrar_cliente(request):
    if request.method == "POST":
        usuario = request.POST.get('nome')
        email = request.POST.get('email')
        contato = request.POST.get('telefone')
        senha = request.POST.get('senha')

        # Verifica se o usuário já existe
        if User.objects.filter(username=usuario).exists():
            return render(request, 'auth_app/cadastrar_cliente.html', {'msg': "Já existe um usuário com esse nome."})

        # Cria um novo superusuário
        User.objects.create_superuser(username=usuario, email=email, password=senha)

        #salvar infor no banco
        Cadastro(usuario=usuario, email=email, contato=contato, senha=senha).save()

        return redirect('home')  # Redireciona para a página de login após o cadastro

    return render(request, 'auth_app/cadastrar_cliente.html', {'msg': ''})