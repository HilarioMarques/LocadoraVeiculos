# LocadoraVeiculos
# 🚗 Sistema Web para Locadora de Carros - Trabalho Final Integrador

Este projeto representa o Trabalho Final Integrador da disciplina de Programação Web do Curso Bacharelado em Ciência da Computação da UNIVERSIDADE ESTADUAL DO PIAUI - UESPI, CAMPUS DRª JOSEFINA DEMES.

O sistema simula a gestão completa de uma locadora de veículos, abrangendo desde o cadastro de clientes e carros até o fluxo transacional de locação.

---

## 🎯 Objetivo

Desenvolver um sistema web completo e funcional, integrando todos os conceitos aprendidos ao longo da disciplina, desde a modelagem de dados até a implementação das principais operações via interface web.

---

## 🔑 Requisitos Mínimos Atendidos

### 1. Autenticação e Segurança
* **Controle de Perfil:** Implementação de autenticação de usuários com diferença de perfil (ex: Admin/Funcionário e Usuário Comum/Cliente).
* **Proteção de Rotas:** Proteção de rotas/sessão para restringir o acesso a funcionalidades específicas.

### 2. Modelagem de Dados
* **Entidades Principais:** O sistema possui, no mínimo, três entidades principais.
    * **Sugestão:** Cliente, Veículo/Carro (Item) e Locação (Transação).
* **Relacionamentos:** Possui relacionamentos claros entre as entidades (Ex.: Cliente aluga Veículo).
* **Validações:** Implementação de validações de integridade e unicidade.
    * Exemplo: Não permitir registro duplicado (como CPF ou placa).
    * Exemplo: Não autorizar transação inválida (como alugar um carro que já está locado).

### 3. Funcionalidades Essenciais (Web)
* **CRUD:** Operações completas de CRUD (Cadastro, Consulta, Alteração e Exclusão) via interface web para pelo menos duas entidades principais (Ex.: Cliente e Veículo/Carro).
* **Fluxo Transacional:** Implementação do fluxo de operação transacional de **Locação**.
* **Histórico/Relatório:** Geração de um histórico ou relatório básico via web.
    * Exemplo: Histórico de locações do usuário ou consulta por período.

---

## 🛠️ Requisitos Técnicos

* **Framework:** Uso do framework **Flask** (Python).
* **Banco de Dados:** Uso obrigatório e efetivo de um **Banco de Dados Relacional**.
* **Interface:** Todo o fluxo de uso ocorre pela interface web criada pelo grupo.

---

## 📝 Documentação e Entregas

Os seguintes artefatos devem ser entregues:

| Item de Entrega | Descrição |
| :--- | :--- |
| **Modelagem de Dados** | MER, DER e scripts SQL de criação do banco. A modelagem deve ser completa, com indicação de chaves, restrições e tipos de dados. |
| **Código-Fonte** | Repositório ou arquivos organizados com o código-fonte do sistema web funcional. |
| **Relatório** | Documento em PDF explicando o projeto, o cenário escolhido, decisão de modelagem, fluxos principais e telas funcionais. |
| **Apresentação** | Prints das páginas principais e exemplos de uso. |
