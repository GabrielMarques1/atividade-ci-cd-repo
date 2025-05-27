# Atividade Prática – API de Livros com Python + CI/CD + Render

Este repositório contém o código para uma API simples de gerenciamento de livros, desenvolvida em Python puro, como parte de uma atividade prática sobre CI/CD e deploy.

## Objetivo

O objetivo principal é criar uma API funcional com as seguintes características:

*   **Rotas:**
    *   `GET /books`: Retorna a lista completa de livros.
    *   `GET /books/<id>`: Retorna um livro específico pelo seu ID.
    *   `POST /books`: Adiciona um novo livro à lista.
*   **Tecnologia:** Python puro (sem frameworks), utilizando listas em memória para armazenamento de dados.
*   **CI/CD:** Configuração de Integração Contínua e Entrega Contínua utilizando GitHub Actions.
*   **Deploy:** Deploy automatizado na plataforma Render.com via webhook.

## Estrutura do Projeto

```
. 
├── .github/
│   └── workflows/
│       └── main.yml      # Workflow do GitHub Actions para CI/CD
├── src/
│   └── server.py       # Código principal da API
├── requirements.txt    # Arquivo de dependências (vazio neste caso)
└── README.md           # Este arquivo
```



1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/GabrielMarques1/Api-CI-CD.git
    cd Api-CI-CD
    ```
2.  **Execute o servidor:**
    ```bash
    python src/server.py
    ```
    O servidor estará rodando em `http://localhost:8000`.

3.  **Teste as rotas (usando curl ou Postman):**
    *   `curl http://localhost:8000/books`
    *   `curl http://localhost:8000/books/1`
    *   `curl -X POST -H "Content-Type: application/json" -d '{"title": "Novo Livro", "author": "Autor Desconhecido"}' http://localhost:8000/books`



O arquivo `.github/workflows/main.yml` contém a configuração do GitHub Actions.

1.  **Validação:** A cada `push` na branch `main`, o workflow valida a sintaxe do código Python (`python -m py_compile src/server.py`).
