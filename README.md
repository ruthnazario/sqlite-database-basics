# 🗄️ SQLite Database Basic

Projeto desenvolvido como um estudo introdutório de **banco de dados SQLite**, com o objetivo de compreender na prática como criar, armazenar, consultar e excluir informações em um banco de dados.

Este foi meu primeiro contato prático com SQLite, utilizando Python para realizar as operações e ferramentas de apoio para visualizar e acompanhar os dados armazenados.

## 🎯 Objetivo

Vivenciar na prática os conceitos básicos de banco de dados, criando uma aplicação simples para cadastro e exclusão de pessoas.

O projeto permite:

* Cadastrar uma pessoa;
* Armazenar nome, idade e e-mail;
* Salvar as informações em um banco de dados SQLite;
* Excluir informações cadastradas;
* Visualizar os dados armazenados no banco.

## 🛠️ Tecnologias e ferramentas

* **Python**
* **SQLite**
* **DB Browser for SQLite (DB4S)**
* **Visual Studio Code**
* **Extensão SQLite para VS Code**

## 📂 Estrutura do projeto

```text
sqlite-database-basic/
│
├── cadastroPessoas.py
├── delete.py
├── pessoa.db
└── README.md
```

### `cadastroPessoas.py`

Responsável pelo cadastro das pessoas e pelo armazenamento das informações no banco de dados.

Os dados cadastrados são:

* Nome
* Idade
* E-mail

### `delete.py`

Responsável pela exclusão de informações cadastradas no banco de dados.

### `pessoa.db`

Banco de dados SQLite criado durante a execução do projeto, responsável por armazenar os dados cadastrados.

### `README.md`

Documentação do projeto.

## 🗃️ Banco de dados

O projeto utiliza o **SQLite**, um banco de dados relacional leve que armazena os dados em um único arquivo.

Para visualizar e acompanhar os registros, utilizei o **DB Browser for SQLite (DB4S)** e a extensão SQLite no Visual Studio Code.

## 📚 O que aprendi

Durante o desenvolvimento deste projeto, pude praticar conceitos básicos de banco de dados, como:

* Criação de um banco de dados SQLite;
* Criação e utilização de tabelas;
* Inserção de dados;
* Armazenamento de informações;
* Exclusão de registros;
* Utilização de comandos SQL;
* Integração entre Python e SQLite;
* Visualização e gerenciamento do banco de dados.

## 🚀 Próximos passos

Este projeto representa o início dos meus estudos em banco de dados. Como próximos passos, pretendo evoluir o projeto adicionando:

* Consulta de registros;
* Atualização de dados;
* Validação das informações;
* CRUD completo;
* Melhor organização do código;
* Integração com outros projetos em Python e Java.

---

### 👩‍💻 Sobre o projeto

Este projeto foi desenvolvido como parte dos meus estudos em **Desenvolvimento de Sistemas**, com o objetivo de aprender e praticar conceitos fundamentais de banco de dados utilizando SQLite e Python.
