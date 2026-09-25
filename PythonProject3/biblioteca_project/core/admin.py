from django.contrib import admin
from .models import PerfilUsuario, Livro, Emprestimo

admin.site.register(PerfilUsuario)
admin.site.register(Livro)
admin.site.register(Emprestimo)
