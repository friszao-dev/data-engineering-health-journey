Data Engineering Health Journey - Pipeline DATASUS

Este repositório documenta a construção de um ecossistema de dados focado no setor de saúde pública brasileiro. O objetivo é transformar dados brutos do DATASUS (Leitos Hospitalares) em informação estratégica através de um pipeline moderno de engenharia de dados.
- Arquitetura e Estratégia

O projeto adota a filosofia ELT (Extract, Load, Transform), priorizando a ingestão bruta (RAW) para garantir a integridade dos dados antes da modelagem analítica.
Estrutura do Repositório

A organização segue padrões de projetos reais de engenharia de software:

.
├── infra/            # Infraestrutura como Código (Docker Compose) [cite: 6, 16]
├── src/              # Código fonte do pipeline [cite: 7]
│   ├── ingestion/    # Scripts Python para carga bruta (RAW) [cite: 8, 17]
│   ├── dbt_project/  # Transformação e Star Schema (Futuro) [cite: 9, 30]
│   └── dashboard/    # Visualização de dados (Futuro) [cite: 10, 37]
├── docs/             # Regras de negócio e documentação técnica [cite: 11]
└── README.md         # Documentação principal [cite: 12]

- Tecnologias e Infraestrutura

    Banco de Dados: PostgreSQL 17 (Otimizado para persistência de grandes volumes).

    Interface de Dados: pgAdmin 4 (Administração e execução de queries SQL).

    Orquestração de Infra: Docker Compose (Isolamento de serviços e redes internas).

    Persistência: Volumes Docker configurados para garantir a sobrevivência dos dados ao ciclo de vida dos containers.

- Como Executar o Ambiente
1. Pré-requisitos

    Docker Desktop instalado e rodando.

    Git para clonagem do repositório.

2. Subindo a Infraestrutura

Navegue até a pasta de infraestrutura e inicie os serviços:
Bash

cd infra
docker-compose up -d

Este comando subirá automaticamente o banco de dados e a interface de gerenciamento.
3. Acesso

    pgAdmin: http://localhost:8080 (Credenciais configuradas no docker-compose.yml).

    PostgreSQL: Disponível na porta 5432.

- Roadmap de Desenvolvimento (Mês 1)

    Semanas 1-2 (Concluído): Estruturação do repositório e implementação da infraestrutura persistente via Docker Compose.

    Semanas 3-4 (Em progresso): Desenvolvimento do script ingest_sus.py utilizando Python (Pandas + SQLAlchemy) para automação da carga bruta (Landing Zone).

    Diário: Resolução de problemas de lógica SQL para garantir maestria na manipulação dos dados de saúde.

- Decisões de Engenharia

    Foco na Resiliência: A infraestrutura foi testada sob falha (simulação de docker-compose down e reinicialização de hardware) para validar o mapeamento de volumes físicos.

    Abordagem de Carga RAW: Decidimos não normalizar dados durante a ingestão com Python para manter a rastreabilidade da origem (Single Source of Truth).

Licença

Este projeto está sob a licença MIT License.