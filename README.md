# 📰 Dio Blog

Projeto acadêmico desenvolvido como parte dos estudos na **Digital Innovation One (DIO)**, com o objetivo de criar um blog simples em Python, estruturado em camadas e com boas práticas de organização de código.

---

## 🚀 Objetivo

Demonstrar o uso de **Programação Orientada a Objetos** e **arquitetura modular** na construção de uma aplicação web do tipo **CRUD (Create, Read, Update, Delete)** para posts de blog.

---

## 🧩 Estrutura do Projeto

```
dio-blog/
│
├── controllers/     # Camada responsável pela lógica de controle e regras de negócio
├── schemas/         # Definição dos modelos de dados (ex: Pydantic ou dataclasses)
├── views/           # Rotas / endpoints da aplicação
├── main.py          # Ponto de entrada principal do sistema
├── pyproject.toml   # Configuração do projeto e dependências (Poetry)
├── poetry.lock      # Versões travadas das dependências
└── LICENSE          # Licença MIT
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.12+**
- **FastAPI** (ou outro framework web conforme implementação)
- **Pydantic** — para validação de dados
- **Uvicorn** — servidor de aplicação ASGI
- **Poetry** — gerenciamento de dependências e ambiente virtual

---

## ⚙️ Instalação e Execução

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/estevaoMG/dio-blog.git
cd dio-blog
```

### 2️⃣ Instalar dependências

Se estiver usando **Poetry**:

```bash
poetry install
```

### 3️⃣ Executar a aplicação

```bash
poetry run uvicorn main:app --reload
```

Depois, acesse em seu navegador:

```
http://localhost:8000
```

---

## 📚 Endpoints (Exemplo)

| Método | Rota           | Descrição                |
|--------|----------------|--------------------------|
| GET    | `/posts`        | Lista todos os posts     |
| GET    | `/posts/{id}`   | Retorna um post específico |
| POST   | `/posts`        | Cria um novo post        |
| PUT    | `/posts/{id}`   | Atualiza um post         |
| DELETE | `/posts/{id}`   | Exclui um post           |

---

## 🧪 Testes (opcional)

Se forem implementados testes, podem ser executados com:

```bash
pytest
```

---

## 🧑‍💻 Autor

**Estevão Gouveia**  
📘 Projeto acadêmico — DIO  
🔗 [GitHub](https://github.com/estevaoMG)

---

## 🪪 Licença

Este projeto está sob a licença [MIT](./LICENSE).

---

> Projeto criado para fins educacionais — explorando boas práticas de desenvolvimento em Python com arquitetura organizada.
