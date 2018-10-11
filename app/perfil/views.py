from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Perfil

# Create your views here.
def index(request):
    return render(request, 'app/index.html')


def editar(request, id):
    usuario = User.objects.get(id=id)
    return render(request, 'app/editar-perfil.html', {'usuario': usuario})


def salvar(request, id):
    idade = request.POST['idade']
    endereco = request.POST['endereco']
    usuario = User.objects.get(id=id) 
    usuario.perfil.idade = idade
    usuario.perfil.endereco = endereco
    usuario.save()
    return HttpResponseRedirect('/')