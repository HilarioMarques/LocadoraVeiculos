# LocadoraVeiculos
## 🚗 Sistema Web para Locadora de Carros - Trabalho Final

Este é o projeto final integrador para a disciplina de Programação Web, desenvolvido utilizando o framework Flask e um banco de dados relacional. O sistema simula a gestão completa de uma locadora de veículos, abrangendo desde o cadastro de clientes e carros até o fluxo transacional de locação.

---

### 🎯 Objetivo

[cite_start]Desenvolver um sistema web completo e funcional, integrando modelagem de dados, *back-end* (Python/Flask) e *front-end* (HTML/CSS/JS) para atender aos requisitos mínimos da disciplina[cite: 8, 9, 10].

---

### 🔑 Requisitos Mínimos Atendidos

[cite_start]O sistema foi estruturado para cumprir todas as exigências estabelecidas no trabalho[cite: 15].

#### [cite_start]1. Autenticação e Segurança [cite: 16]
* [cite_start]**Controle de Perfil:** Implementação de autenticação com diferença de perfil (ex: **Admin/Funcionário** e **Usuário Comum/Cliente**)[cite: 17].
* [cite_start]**Proteção de Rotas:** Gerenciamento de sessão e proteção de rotas para garantir que apenas usuários autorizados acessem determinadas funcionalidades[cite: 18].

#### [cite_start]2. Modelagem e Entidades [cite: 19]
[cite_start]O sistema utiliza um mínimo de três entidades principais com relacionamentos claros[cite: 19, 21]:
* **Cliente:** Entidade para gerenciar as informações dos locatários.
* **Veículo/Carro:** Entidade para gerenciar a frota disponível para locação.
* [cite_start]**Locação:** Entidade transacional que registra o aluguel do Veículo pelo Cliente[cite: 20, 22].

#### [cite_start]3. Operações CRUD [cite: 23]
[cite_start]O sistema permite as quatro operações básicas (Cadastro, Consulta, Alteração e Exclusão) via interface web para, no mínimo, as entidades **Cliente** e **Veículo/Carro**[cite: 23, 24].

#### [cite_start]4. Fluxo Transacional e Validação [cite: 25]
* [cite_start]**Fluxo de Locação:** Implementação de um fluxo de operação transacional para registrar o aluguel de um carro[cite: 25, 26].
* [cite_start]**Validações:** Uso de validações para garantir a integridade e unicidade dos dados[cite: 27].
    * [cite_start]Exemplo: Impedir o registro duplicado de CPF ou placa de veículo[cite: 29].
    * [cite_start]Exemplo: Não permitir a Locação de um Veículo que já está alugado[cite: 29].

#### [cite_start]5. Relatórios e Histórico [cite: 30]
* [cite_start]**Relatório Básico:** Geração de relatórios ou visualização de histórico via interface web[cite: 30].
    * [cite_start]Exemplo: Histórico de locações do Cliente ou visualização do *status* dos veículos (disponível/locado)[cite: 31].

---

### 🛠️ Tecnologias e Entregas

| Categoria | Descrição | Requisito de Entrega |
| :--- | :--- | :--- |
| **Back-end** | [cite_start]Python, Framework Flask [cite: 13] | [cite_start]Código-fonte do sistema funcional [cite: 40] |
| **Banco de Dados** | [cite_start]Uso obrigatório de Banco de Dados Relacional [cite: 14] | [cite_start]Scripts SQL de criação do banco [cite: 39] |
| **Modelagem** | [cite_start]MER e DER completos com indicação de chaves, restrições e tipos [cite: 32, 33] | [cite_start]MER e DER (Documento ou Imagens) [cite: 39] |
| **Documentação** | [cite_start]Relatório em PDF com explicação do cenário, modelagem, fluxos e telas do sistema [cite: 35, 36, 37] | [cite_start]Relatório (PDF) [cite: 41] |
| **Interface** | HTML, CSS, JavaScript | [cite_start]Prints das páginas principais e exemplos de uso [cite: 37, 42] |
