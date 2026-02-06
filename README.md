# Data Engineering Health Journey - Análise DATASUS

![GitHub repo size](https://img.shields.io/github/repo-size/friszao-dev/data-engineering-health-journey)
![GitHub last commit](https://img.shields.io/github/last-commit/friszao-dev/data-engineering-health-journey)
![GitHub issues](https://img.shields.io/github/issues/friszao-dev/data-engineering-health-journey)

Este repositório documenta a primeira fase da minha jornada de transição de carreira para **Engenharia de Dados**.  
O projeto foca na estruturação, tratamento e análise de dados públicos de saúde do Brasil (leitos hospitalares), utilizando tecnologias fundamentais do ecossistema moderno de dados.

---

## 📑 Sumário
- [Tecnologias e Ferramentas](#tecnologias-e-ferramentas)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Etapas do Projeto](#etapas-do-projeto)
  - [1. Configuração do Ambiente (Docker)](#1-configuração-do-ambiente-docker)
  - [2. Aprendizados Técnicos](#2-aprendizados-técnicos)
  - [3. Rotina de Refatoração e Resiliência](#3-rotina-de-refatoração-e-resiliência)
- [Como Executar](#como-executar)
- [Licença](#licença)

---

## Tecnologias e Ferramentas
- **Banco de Dados:** PostgreSQL (Relacional)  
- **Infraestrutura:** Docker & Docker Desktop  
- **IDE de Dados:** DBeaver  
- **Controle de Versão:** Git & GitHub  

---

## Estrutura do Projeto

```
📂 data-engineering-health-journey
├── README.md
├── scripts/           # Scripts SQL e Python
├── docs/              # Documentação e notas técnicas
├── data/              # Dados de entrada (se permitido)
└── docker/            # Configurações de container e volumes
```

---

## Etapas do Projeto

### 1. Configuração do Ambiente (Docker)
Isolamento do ambiente de banco de dados utilizando containers, garantindo persistência com **Volumes**.

> **Nota Técnica:** Devido à atualização para PostgreSQL 18+, ajustei o mapeamento do diretório principal (`/var/lib/postgresql`) para permitir que o sistema gerencie subpastas de versão e upgrades de forma nativa e segura.

#### Comando para subir o container (PowerShell):

```powershell
docker run --name postgres-saude `
  -e POSTGRES_PASSWORD=minhasenha123 `
  -p 5432:5432 `
  -v pgdata_saude:/var/lib/postgresql `
  -d postgres
```

---

### 2. Aprendizados Técnicos

1. **Persistência e Infraestrutura**
   - Implementação de Docker Volumes para desacoplar dados do ciclo de vida do container.
   - Troubleshooting: Resolução de conflitos de montagem em versões recentes do PostgreSQL.

2. **Manipulação de Dados (SQL)**
   - Padronização de nomenclatura de objetos em `snake_case`.
   - Diferenciação entre filtros de linha (`WHERE`) e filtros de agregação (`HAVING`).
   - Uso de Window Functions (`ROW_NUMBER() OVER`) para criação de rankings.
   - Implementação de CTEs (Common Table Expressions) para maior legibilidade e manutenção de queries complexas.

3. **Qualidade de Dados & Troubleshooting**
   - Correção de tipagem: resolução do erro de importação [22P02], onde colunas de texto foram interpretadas como tipo `int`.
   - Saneamento de registros duplicados e identificação de inconsistências em colunas de capacidade.

---

### 3. Rotina de Refatoração e Resiliência

Para garantir confiabilidade da infraestrutura e maestria técnica:

- **Reconstrução do Ambiente:** Exclusão e recriação de containers e volumes para validar idempotência.  
- **Data Drill-down:** Repetição manual de queries complexas para consolidar lógica de negócio.  
- **Validação de Conexões:** Reconfiguração do DBeaver do zero para dominar mapeamento de drivers e schemas.

Foco atual: Finalizando fundamentos de SQL e preparando automação com Python.

---

## Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/friszao-dev/data-engineering-health-journey.git
cd data-engineering-health-journey
```

2. Suba o container Docker:

```powershell
docker run --name postgres-saude `
  -e POSTGRES_PASSWORD=minhasenha123 `
  -p 5432:5432 `
  -v pgdata_saude:/var/lib/postgresql `
  -d postgres
```

3. Conecte-se ao banco via **DBeaver** ou outro cliente SQL.  

4. Execute scripts na pasta `scripts/` conforme necessário.

---

## Licença

Este projeto está sob a licença **MIT License**. Consulte o arquivo `LICENSE` para mais detalhes.
