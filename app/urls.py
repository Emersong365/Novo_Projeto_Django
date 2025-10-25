from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_alunos, name='lista_alunos'),                # Listagem
    path('novo/', views.aluno_create, name='aluno_create'),          # Criar novo
    path('<int:pk>/', views.aluno_detalhe, name='aluno_detalhe'),    # Detalhes
    path('<int:pk>/editar/', views.aluno_update, name='aluno_update'), # Editar
    path('<int:pk>/excluir/', views.aluno_delete, name='aluno_delete'),# Excluir
]
