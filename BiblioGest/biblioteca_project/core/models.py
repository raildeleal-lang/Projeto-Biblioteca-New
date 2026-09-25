from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, date


# 1. MODELO DE USUÁRIO (Estendendo o usuário padrão do Django)
class PerfilUsuario(models.Model):
    TIPO_CHOICES = [
        ('ALUNO', 'Aluno'),
        ('PROFESSOR', 'Professor'),
        ('SERVIDOR', 'Servidor'),
    ]

    # Vincula com o sistema de Login nativo do Django
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    matricula = models.CharField(max_length=20, unique=True)
    tipo = models.CharField(max_length=15, choices=TIPO_CHOICES, default='ALUNO')

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.tipo})"


# 2. MODELO DE LIVRO
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    disponivel = models.BooleanField(default=True)  # Controle de status (🟢/🔴)

    def __str__(self):
        return self.titulo


# 3. MODELO DE EMPRÉSTIMO (Com a regra de 8 dias)
def data_devolucao_padrao():
    # Retorna automaticamente a data de hoje + 8 dias
    return date.today() + timedelta(days=8)


class Emprestimo(models.Model):
    usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(auto_now_add=True)  # Salva a data de hoje na criação
    data_devolucao_prevista = models.DateField(default=data_devolucao_padrao)  # Regra dos 8 dias
    devolvido = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.livro.titulo} -> {self.usuario.user.first_name}"
