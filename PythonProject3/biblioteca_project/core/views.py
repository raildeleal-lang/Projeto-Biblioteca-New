from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.models import User
from .models import PerfilUsuario, Livro
from .models import Emprestimo
from django.shortcuts import get_object_or_404


# 1. Definição do Formulário no Django
class CadastroUsuarioForm(forms.Form):
    nome = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primeiro Nome'}))
    sobrenome = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: carlos.silva'}))
    password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite a senha'}))
    matricula = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2026123'}))
    tipo = forms.ChoiceField(choices=PerfilUsuario.TIPO_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))


# 2. As funções de visualização das páginas (Views)
def home(request):
    return render(request, 'core/home.html')


def lista_livros(request):
    livros_do_banco = Livro.objects.all()
    return render(request, 'core/lista_livros.html', {'livros': livros_do_banco})


def lista_usuarios(request):
    usuarios_do_banco = PerfilUsuario.objects.all()
    return render(request, 'core/lista_usuarios.html', {'usuarios': usuarios_do_banco})


def cadastrar_usuario(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():  # <-- CORRIGIDO AQUI! (De 'is_validate' para 'is_valid')
            # Cria o usuário nativo do Django para o login
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['nome'],
                last_name=form.cleaned_data['sobrenome']
            )
            # Vincula ao perfil com matrícula e tipo (Aluno/Professor/Servidor)
            PerfilUsuario.objects.create(
                user=user,
                matricula=form.cleaned_data['matricula'],
                tipo=form.cleaned_data['tipo']
            )
            return redirect('lista_usuarios')  # Redireciona para a lista após salvar
    else:
        form = CadastroUsuarioForm()

    return render(request, 'core/cadastro_usuario.html', {'form': form})


class CadastroLivroForm(forms.Form):
    titulo = forms.CharField(max_length=200,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título da Obra'}))
    autor = forms.CharField(max_length=150,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Autor'}))


# 2. Adicione esta nova função de visualização ao final do arquivo:
def cadastrar_livro(request):
    if request.method == 'POST':
        form = CadastroLivroForm(request.POST)
        if form.is_valid():
            Livro.objects.create(
                titulo=form.cleaned_data['titulo'],
                autor=form.cleaned_data['autor'],
                disponivel=True  # Todo livro novo começa na estante disponível
            )
            return redirect('lista_livros')  # Volta para o acervo após salvar
    else:
        form = CadastroLivroForm()

    return render(request, 'core/cadastro_livro.html', {'form': form})


# 1. Formulário de Empréstimo
class CadastroEmprestimoForm(forms.Form):
    # Mostra apenas os usuários cadastrados
    usuario = forms.ModelChoiceField(
        queryset=PerfilUsuario.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Selecione o Usuário"
    )
    # Mostra apenas os livros que estão atualmente disponíveis na estante
    livro = forms.ModelChoiceField(
        queryset=Livro.objects.filter(disponivel=True),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Selecione o Livro"
    )


def lista_emprestimos(request):
    # O .filter(ativo=True) garante que o histórico antigo fique escondido aqui
    emprestimos = Emprestimo.objects.filter(ativo=True).order_by('-data_emprestimo')
    return render(request, 'core/lista_emprestimos.html', {'emprestimos': emprestimos})


class CadastroEmprestimoForm(forms.Form):
    usuario = forms.ModelChoiceField(
        queryset=PerfilUsuario.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select', 'style': 'padding: 10px; border-radius: 6px; border: 1px solid #cbd5e1; width: 100%; font-size: 0.95rem; margin-top: 5px;'}),
        label="Quem vai levar? (Usuário)"
    )
    livro = forms.ModelChoiceField(
        queryset=Livro.objects.filter(disponivel=True),
        widget=forms.Select(attrs={'class': 'form-select', 'style': 'padding: 10px; border-radius: 6px; border: 1px solid #cbd5e1; width: 100%; font-size: 0.95rem; margin-top: 5px;'}),
        label="Qual livro será retirado?"
    )


def cadastrar_emprestimo(request):
    if request.method == 'POST':
        form = CadastroEmprestimoForm(request.POST)
        if form.is_valid():
            livro_selecionado = form.cleaned_data['livro']

            # Cria o registro do empréstimo (regra de 8 dias automática)
            Emprestimo.objects.create(
                usuario=form.cleaned_data['usuario'],
                livro=livro_selecionado
            )

            # Muda o status do livro para Indisponível (🔴 Emprestado)
            livro_selecionado.disponivel = False
            livro_selecionado.save()

            return redirect('lista_emprestimos')
    else:
        form = CadastroEmprestimoForm()

    return render(request, 'core/cadastro_emprestimo.html', {'form': form})


def devolver_livro(request, emprestimo_id):
    # Busca o empréstimo correto no banco usando o ID recebido
    from django.shortcuts import get_object_or_404
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)

    # Pega o livro que estava vinculado a esse empréstimo
    livro = emprestimo.livro

    # Regra de negócio: Devolve o livro para a estante
    livro.disponivel = True
    livro.save()

    emprestimo.ativo = False
    emprestimo.devolvido = True
    emprestimo.save()

    return redirect('lista_emprestimos')


def editar_usuario(request, usuario_id):
    # 1. Busca o perfil do usuário pelo ID recebido
    perfil = get_object_or_404(PerfilUsuario, id=usuario_id)
    user = perfil.user  # Pega os dados de login vinculados (nome, sobrenome, etc.)

    if request.method == 'POST':
        # 2. Se enviou o formulário, carrega os novos dados digitados
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            # 3. Atualiza os dados do usuário nativo do Django
            user.first_name = form.cleaned_data['nome']
            user.last_name = form.cleaned_data['sobrenome']
            user.username = form.cleaned_data['username']
            # Se digitou uma nova senha, atualiza ela com segurança
            if form.cleaned_data['password']:
                user.set_password(form.cleaned_data['password'])
            user.save()

            # 4. Atualiza os dados de matrícula e vínculo
            perfil.matricula = form.cleaned_data['matricula']
            perfil.tipo = form.cleaned_data['tipo']
            perfil.save()

            return redirect('lista_usuarios') # Volta para a listagem
    else:
        # 5. Se está abrindo a página pela primeira vez, preenche o formulário com os dados atuais
        dados_atuais = {
            'nome': user.first_name,
            'sobrenome': user.last_name,
            'username': user.username,
            'matricula': perfil.matricula,
            'tipo': perfil.tipo
        }
        form = CadastroUsuarioForm(initial=dados_atuais)

    return render(request, 'core/cadastro_usuario.html', {'form': form, 'editando': True})


def editar_livro(request, livro_id):
    # 1. Busca o livro pelo ID
    livro = get_object_or_404(Livro, id=livro_id)

    if request.method == 'POST':
        # 2. Se enviou o formulário, pega as alterações
        form = CadastroLivroForm(request.POST)
        if form.is_valid():
            livro.titulo = form.cleaned_data['titulo']
            livro.autor = form.cleaned_data['autor']
            livro.save() # Salva no banco de dados
            return redirect('lista_livros')
    else:
        # 3. Se está abrindo a página, preenche com o Título e Autor atuais
        dados_atuais = {
            'titulo': livro.titulo,
            'autor': livro.autor
        }
        form = CadastroLivroForm(initial=dados_atuais)

    return render(request, 'core/cadastro_livro.html', {'form': form, 'editando': True})


def excluir_usuario(request, usuario_id):
    # Busca o perfil do usuário pelo ID
    perfil = get_object_or_404(PerfilUsuario, id=usuario_id)
    # Como deletar o User do Django também deleta o perfil (CASCADE), removemos o User
    perfil.user.delete()
    return redirect('lista_usuarios')

def excluir_livro(request, livro_id):
    # Busca o livro pelo ID e deleta do banco
    livro = get_object_or_404(Livro, id=livro_id)
    livro.delete()
    return redirect('lista_livros')


