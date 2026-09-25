# 🟢 BiblioGest: Sistema de Gestão de Acervo Escolar

O **BiblioGest** é uma aplicação web desenvolvida para modernizar e digitalizar o controle de acervos, cadastros de usuários e fluxos de empréstimos da biblioteca escolar. O sistema substitui os antigos registros manuais por uma plataforma ágil, responsiva e integrada a um banco de dados relacional.

---

## 🚀 Como Executar a Aplicação (Roteiro Passo a Passo)

Siga os comandos abaixo no terminal do seu editor (como o PyCharm ou VS Code) para ativar o ambiente virtual e iniciar o servidor local do sistema:

```bash
# 1. Ative o ambiente virtual (Virtual Environment)
.\.venv\Scripts\Activate.ps1

# 2. Acesse a pasta raiz do projeto Django
cd .\biblioteca_project\

# 3. Inicialize os componentes principais (se aplicável)
python main.py

# 4. Inicie o servidor de desenvolvimento do Django
python manage.py runserver
```

Após iniciar o servidor, abra o seu navegador de internet e acesse o endereço local:
👉 **[http://127.0.0](http://127.0.0)**

---

## 🛠️ Tecnologias e Arquitetura Utilizadas

A aplicação foi construída utilizando divisões claras entre regras de negócio e interface:

*   **Back-End (Inteligência do Sistema):**
    *   **Python:** Linguagem base para codificação de toda a lógica do servidor.
    *   **Django Framework:** Estrutura para gerenciamento de rotas seguras, validação de formulários e mapeamento de dados.
    *   **SQLite:** Banco de dados relacional integrado para persistência e armazenamento das informações.
*   **Front-End (Interface Visual):**
    *   **HTML5 & CSS3:** Estruturação semântica e customização estética global.
    *   **Bootstrap 5:** Componentes responsivos, tabelas limpas e botões institucionais na paleta verde-escura.
    *   **JavaScript:** Interceptação lógica de eventos e manipulação dinâmica de elementos (janela modal de confirmação).

---

## 📊 Módulos e Funcionalidades do CRUD (Sem Django Admin)

O sistema opera com independência completa do painel nativo do Django, possuindo telas próprias para manipulação de dados:

*   **👥 Módulo de Usuários:** Cadastro, consulta em tabela estruturada e edição de dados de Alunos, Professores e Servidores.
*   **📚 Módulo de Livros (Acervo):** Catálogo detalhado com indicação visual automatizada de status (🟢 Disponível / 🔴 Emprestado).
*   **📅 Controle de Empréstimos:** Vinculação digital entre leitores e obras, com cálculo automatizado de prazo de **devolução limite para 8 dias**.
*   **✅ Sistema de Devoluções (Histórico):** Lógica integrada no back-end que altera o status do livro de volta para disponível e desativa o empréstimo ativo, retendo as informações no histórico do banco de dados de forma segura.
*   **⚠️ Interatividade com JavaScript:** Validação e segurança através de um modal customizado em JavaScript que impede a exclusão acidental de registros nas tabelas.

---

## 📜 Informações do Projeto Acadêmico
*   **Instituição:** Universidade Federal Rural da Amazônia (UFRA)
*   **Campus:** Capitão Poço – Polo São Miguel do Guamá
*   **Curso:** Bacharelado em Sistemas de Informação
*   **Disciplina:** Desenvolvimento Web
*   **Equipe de Desenvolvimento:** Jennifer dos Reis Lima & Railde Leal dos Santos
