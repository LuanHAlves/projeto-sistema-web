from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect
from usuarios.forms import UserModelForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.template import RequestContext
from django.contrib import messages


def home(request):
    form = UserModelForm(request.POST or None)
    context = {'form':form}
    if request.method == 'POST':
        
        if form.is_valid():
            try:
                form.save()
                return redirect('/cadastro_sucesso')
            except IntegrityError:
                messages.info(request, 'Usuário e/ou Email já cadastrados.  Por favor, tente novamente!')
                return render_to_response('usuarios/index.html', locals(), context_instance=RequestContext(request))   
    
    return render(request, 'usuarios/index.html', context)


@login_required
def area_logada(request):
   return render(request, 'usuarios/AreaLogada.html', {})


def entrar(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return HttpResponseRedirect("/AreaLogada") 
    return render(request, 'usuarios/login.html', {'form': form })


@login_required
def sair(request):
    logout(request)
    return HttpResponseRedirect('/login')



def cadastro_sucesso(request):
   return render(request, 'usuarios/cadastro_sucesso.html', {})



def sobre(request):
   return render(request, 'usuarios/sobre.html', {})
