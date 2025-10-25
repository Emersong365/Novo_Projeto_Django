from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno
from .forms import AlunoForm
from django.contrib import messages  # Para o desafio de mensagens

# Listagem
def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'app/lista.html', {'alunos': alunos})

# Criar
def aluno_create(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Aluno criado com sucesso!")  # Desafio
            return redirect('lista_alunos')
    else:
        form = AlunoForm()
    return render(request, 'app/aluno_form.html', {'form': form})

# Detalhes
def aluno_detalhe(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    return render(request, 'app/aluno_detalhe.html', {'aluno': aluno})

# Editar
def aluno_update(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            messages.success(request, "Aluno atualizado com sucesso!")  # Desafio
            return redirect('lista_alunos')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'app/aluno_form.html', {'form': form})

# Excluir
def aluno_delete(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        messages.success(request, "Aluno excluído com sucesso!")  # Desafio
        return redirect('lista_alunos')
    return render(request, 'app/aluno_confirm_delete.html', {'aluno': aluno})
