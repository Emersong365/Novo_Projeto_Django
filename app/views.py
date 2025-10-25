from django.shortcuts import render
from .models import Aluno

def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'app/lista.html', {'alunos': alunos})
from django.shortcuts import render

# Create your views here.
