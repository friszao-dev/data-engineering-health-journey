# Data Engineering Health Journey - Pipeline DATASUS

Este repositório documenta a construção de um ecossistema de dados focado no setor de saúde pública brasileiro. O objetivo é transformar dados brutos do DATASUS em informação estratégica através de um pipeline moderno de engenharia de dados.

## Arquitetura e Estratégia

O projeto adota a filosofia ELT (Extract, Load, Transform), priorizando a ingestão bruta (RAW) para garantir a integridade dos dados antes da modelagem analítica.

## Estrutura do Repositório

A organização segue padrões de projetos reais de engenharia de dados:

```text
.
├── infra/            # Infraestrutura como Código (Docker Compose)
├── src/              # Código fonte do pipeline
│   ├── ingestion/    # Scripts Python para carga bruta (RAW)
│   ├── dbt_project/  # Transformação e Star Schema (Futuro)
│   └── dashboard/    # Visualização de dados (Futuro)
├── docs/             # Regras de negócio e documentação técnica
└── README.md         # Documentação principal
```


## Tecnologias e Infraestrutura

- Banco de Dados: PostgreSQL 17
- Interface de Dados: pgAdmin 4
- Orquestração de Infraestrutura: Docker Compose
- Persistência: Volumes Docker para garantir a sobrevivência dos dados ao ciclo de vida dos containers
- Controle de Versão: Git e GitHub

## Como Executar o Ambiente

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

## Roadmap de Desenvolvimento (Módulo 1)

- Etapas 1-2 (Concluído):
  - Estruturação do repositório
  - Implementação da infraestrutura persistente com Docker Compose

- Etapas 3-4 (Em progresso):
  - Desenvolvimento do script ingest_sus.py utilizando Python (Pandas + SQLAlchemy)
  - Automação da carga bruta dos dados do DATASUS (Landing Zone)

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
