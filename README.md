# Data Engineering Health Journey - Pipeline DATASUS

Este repositório documenta a construção de um ecossistema de dados focado no setor de saúde pública brasileiro. O objetivo é transformar dados brutos do DATASUS em informação estratégica através de um pipeline moderno de engenharia de dados.

## Arquitetura e Estratégia

O projeto adota a filosofia ELT (Extract, Load, Transform), priorizando a ingestão bruta (RAW) para garantir a integridade dos dados antes da modelagem analítica.

## Fluxo de Dados:

[CSV Raw] ➔ [Python + Logging] ➔ [.env Secrets] ➔ [PostgreSQL (Bronze)] ➔ [Analytic CTEs].

## Estrutura do Repositório

A organização segue padrões de projetos reais de engenharia de dados:

```text
.
├── data/
│   └── raw/
├── infra/
├── src/
│   ├── ingestion/     # RAW layer
│   ├── transformation/ # STAGING / MART (dbt)
│   └── analytics/     # Dashboard
├── docs/
└── README.md

```


## Tecnologias e Infraestrutura

- Python Libraries: Pandas, SQLAlchemy, python-dotenv, logging
- Banco de Dados: PostgreSQL 17
- Interface de Dados: pgAdmin 4
- Orquestração de Infraestrutura: Docker Compose
- Persistência: Volumes Docker para garantir a sobrevivência dos dados ao ciclo de vida dos containers
- Controle de Versão: Git e GitHub

## Como Executar o Ambiente

### Configuração de Variáveis de Ambiente
O projeto utiliza um arquivo `.env` para gestão de credenciais sensíveis. 
1. Renomeie o arquivo `infra/.env.example` para `infra/.env`.
2. Ajuste as credenciais conforme necessário.

### Pré-requisitos

- Docker Desktop instalado e rodando
- Git para clonagem do repositório

### Subindo a Infraestrutura

```bash
cd infra
docker-compose up -d
```

### Acesso aos Serviços

- pgAdmin: http://localhost:8080
- PostgreSQL: Disponível na porta 5432

### Como Validar a Ingestão
Após rodar o script de ingestão, você pode validar o sucesso executando a query abaixo no pgAdmin ou DBeaver:

```sql
SELECT count(*) FROM raw_leitos;
-- Resultado esperado: 86.147 registros.
```

## Roadmap de Desenvolvimento (Módulo 1)

- **Fase 1: Infraestrutura e Ambiente (Concluído)** 
  - Estruturação do repositório.
  - Implementação da infraestrutura persistente com Docker Compose.
  - Configuração de ambiente virtual isolado (`.venv`) para desenvolvimento Python.

- **Fase 2: Ingestão e Validação RAW (Concluído)** 
  - Desenvolvimento do script `ingest_sus.py` utilizando **Python (Pandas + SQLAlchemy)**.
  - Processamento e carga de **86.147 registros** de leitos hospitalares (CSV) para o PostgreSQL.
  - Implementação de tratamento de strings, padronização de colunas e gestão de nulos com `COALESCE`.
  - Criação de scripts de análise exploratória (`queries_exploratorias.sql`) para validação de métricas de saúde.
  - Implementação de Logging Persistente para rastreabilidade de falhas no pipeline.

- **Fase 3: Qualidade e CI/CD (Em progresso)** ⏳
  - Configuração de Linters (SQLFluff) e automação via GitHub Actions.

- Prática contínua:
  - Resolução diária de problemas de lógica SQL para garantir maestria na manipulação dos dados de saúde

## Decisões de Engenharia

- Foco em Resiliência:
  A infraestrutura foi testada sob simulação de falha, utilizando docker-compose down, exclusão de conexões, reinicialização de hardware durante montagem de queries, para validar o mapeamento de volumes físicos e o perfeito funcionamento. 

- Abordagem de Carga RAW:
  Dados não são normalizados durante a ingestão para manter rastreabilidade.

## Próximos Passos

- Finalizar automação da ingestão
- Iniciar modelagem com dbt
- Evoluir pipeline com foco em qualidade

## Licença

Este projeto está sob a licença MIT License.
