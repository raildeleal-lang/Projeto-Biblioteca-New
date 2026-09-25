from django.contrib import admin
from django.urls import path
from core.views import (
    lista_usuarios, home, lista_livros,
    cadastrar_usuario, cadastrar_livro,
    lista_emprestimos, cadastrar_emprestimo, devolver_livro,
    editar_usuario, editar_livro, excluir_usuario, excluir_livro
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    # Módulo de Usuários
    path('usuarios/', lista_usuarios, name='lista_usuarios'),
    path('usuarios/novo/', cadastrar_usuario, name='cadastrar_usuario'),
    path('usuarios/editar/<int:usuario_id>/', editar_usuario, name='editar_usuario'),
    path('usuarios/excluir/<int:usuario_id>/', excluir_usuario, name='excluir_usuario'),

    # Módulo de Livros
    path('livros/', lista_livros, name='lista_livros'),
    path('livros/novo/', cadastrar_livro, name='cadastrar_livro'),
    path('livros/editar/<int:livro_id>/', editar_livro, name='editar_livro'),
    path('livros/excluir/<int:livro_id>/', excluir_livro, name='excluir_livro'),

    # Módulo de Empréstimos
    path('emprestimos/', lista_emprestimos, name='lista_emprestimos'),
    path('emprestimos/novo/', cadastrar_emprestimo, name='cadastrar_emprestimo'),
    path('emprestimos/devolver/<int:emprestimo_id>/', devolver_livro, name='devolver_livro'),
]
