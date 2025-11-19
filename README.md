# LocadoraVeiculos
# 🚗 Sistema Web para Locadora de Carros - Trabalho Final Integrador

[cite_start]Este projeto representa o Trabalho Final Integrador da disciplina de Programação Web do Curso Bacharelado em Ciência da Computação da UNIVERSIDADE ESTADUAL DO PIAUI - UESPI, CAMPUS DRª JOSEFINA DEMES[cite: 2, 3, 4, 5, 7].

[cite_start]O sistema simula a gestão completa de uma locadora de veículos, abrangendo desde o cadastro de clientes e carros até o fluxo transacional de locação[cite: 12].

---

## 🎯 Objetivo

[cite_start]Desenvolver um sistema web completo e funcional [cite: 9][cite_start], integrando todos os conceitos aprendidos ao longo da disciplina [cite: 9][cite_start], desde a modelagem de dados até a implementação das principais operações via interface web[cite: 10].

---

## 🔑 Requisitos Mínimos Atendidos

[cite_start]O projeto foi criado do zero pelo grupo [cite: 10] [cite_start]e atende obrigatoriamente aos seguintes requisitos mínimos[cite: 15]:

### 1. Autenticação e Segurança
* [cite_start]**Controle de Perfil:** Implementação de autenticação de usuários com diferença de perfil (ex: Admin/Funcionário e Usuário Comum/Cliente)[cite: 16, 17].
* [cite_start]**Proteção de Rotas:** Proteção de rotas/sessão para restringir o acesso a funcionalidades específicas[cite: 18].

### 2. Modelagem de Dados
* [cite_start]**Entidades Principais:** O sistema possui, no mínimo, três entidades principais[cite: 19].
    * [cite_start]**Sugestão:** Cliente, Veículo/Carro (Item) e Locação (Transação)[cite: 20].
* [cite_start]**Relacionamentos:** Possui relacionamentos claros entre as entidades (Ex.: Cliente aluga Veículo)[cite: 21, 22].
* [cite_start]**Validações:** Implementação de validações de integridade e unicidade[cite: 27].
    * [cite_start]Exemplo: Não permitir registro duplicado (como CPF ou placa)[cite: 29].
    * [cite_start]Exemplo: Não autorizar transação inválida (como alugar um carro que já está locado)[cite: 29].

### 3. Funcionalidades Essenciais (Web)
* [cite_start]**CRUD:** Operações completas de CRUD (Cadastro, Consulta, Alteração e Exclusão) via interface web para pelo menos duas entidades principais (Ex.: Cliente e Veículo/Carro)[cite: 23, 24].
* [cite_start]**Fluxo Transacional:** Implementação do fluxo de operação transacional de **Locação**[cite: 25, 26].
* [cite_start]**Histórico/Relatório:** Geração de um histórico ou relatório básico via web[cite: 30].
    * [cite_start]Exemplo: Histórico de locações do usuário ou consulta por período[cite: 31].

---

## 🛠️ Requisitos Técnicos

* [cite_start]**Framework:** Uso do framework **Flask** (Python)[cite: 13].
* [cite_start]**Banco de Dados:** Uso obrigatório e efetivo de um **Banco de Dados Relacional**[cite: 14].
* [cite_start]**Interface:** Todo o fluxo de uso ocorre pela interface web criada pelo grupo[cite: 13].

---

## 📝 Documentação e Entregas

[cite_start]Os seguintes artefatos devem ser entregues[cite: 38]:

| Item de Entrega | Descrição |
| :--- | :--- |
| **Modelagem de Dados** | [cite_start]MER, DER e scripts SQL de criação do banco[cite: 39]. [cite_start]A modelagem deve ser completa, com indicação de chaves, restrições e tipos de dados[cite: 32, 33]. |
| **Código-Fonte** | [cite_start]Repositório ou arquivos organizados com o código-fonte do sistema web funcional[cite: 40]. |
| **Relatório** | [cite_start]Documento em PDF explicando o projeto [cite: 41][cite_start], o cenário escolhido, decisão de modelagem, fluxos principais e telas funcionais[cite: 35, 36, 37]. |
| **Apresentação** | [cite_start]Prints das páginas principais e exemplos de uso[cite: 37, 42]. |
