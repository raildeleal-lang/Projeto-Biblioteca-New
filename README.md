# Projeto-Biblioteca-New
Teste de projeto
# 📚 BiblioGest - Sistema de Gestão de Biblioteca

O **BiblioGest** é uma aplicação web desenvolvida em Django para o gerenciamento de acervos bibliográficos. O sistema permite o cadastro, listagem, edição e exclusão de livros, além de gerenciar os vínculos entre autores, editoras e obras.

---

## 🚀 Funcionalidades

- 🔐 **Autenticação:** Cadastro e login de usuários (se houver).
- 📖 **Gestão de Acervo:** CRUD completo (Criar, Ler, Atualizar e Deletar) de livros.
- 🔗 **Vínculos Inteligentes:** Associação dinâmica entre livros, autores e categorias.
- 🖥️ **Interface Responsiva:** Painel administrativo simples e intuitivo para o usuário.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Django Framework**
- **SQLite** (Banco de dados padrão de desenvolvimento)
- **HTML5 / CSS3 / JavaScript** (Para a interface)

---

## 📦 Como Executar o Projeto Localmente

Siga os passos abaixo para rodar o BiblioGest na sua máquina:

### 1. Clonar o Repositório
```bash
git clone https://github.com
cd bibliogest
```

### 2. Criar e Ativar o Ambiente Virtual
**No Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**No Linux/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as Dependências
```bash
python -m pip install django dj-static
```
*(Caso tenha o arquivo de requerimentos, use: `python -m pip install -r requirements.txt`)*

### 4. Rodar as Migrações do Banco de Dados
```bash
python manage.py migrate
```

### 5. Iniciar o Servidor de Desenvolvimento
```bash
python manage.py runserver
```

Agora, abra o seu navegador e acesse: **`http://127.0.0`**

