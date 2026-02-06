# Data Engineering Health Journey - Análise DATASUS 

Este repositório documenta a primeira fase da minha jornada de transição de carreira para a **Engenharia de Dados**. O projeto foca na estruturação, tratamento e análise de dados públicos de saúde do Brasil (leitos hospitalares), utilizando as tecnologias fundamentais do ecossistema de dados moderno.

---

## Tecnologias e Ferramentas
- **Banco de Dados:** PostgreSQL (Relacional)
- **Infraestrutura:** Docker & Docker Desktop
- **IDE de Dados:** DBeaver
- **Controle de Versão:** Git & GitHub

---

## Etapas do Projeto

### 1. Configuração do Ambiente (Docker)
A primeira etapa consistiu em isolar o ambiente de banco de dados utilizando containers. Evoluí para o uso de **Volumes** para garantir a persistência dos dados. 

> **Nota Técnica:** Devido à atualização para o PostgreSQL 18+, realizei o ajuste no mapeamento do diretório principal (`/var/lib/postgresql`), permitindo que o sistema gerencie subpastas de versão e upgrades de forma nativa e segura.

#### Comando para subir o container (PowerShell):

```powershell
docker run --name postgres-saude `
  -e POSTGRES_PASSWORD=minhasenha123 `
  -p 5432:5432 `
  -v pgdata_saude:/var/lib/postgresql `
  -d postgres

Aprendizados Técnicos

    Persistência e Infraestrutura

        Implementação de Docker Volumes para desacoplar dados do ciclo de vida do container.
        Troubleshooting: Resolução de conflitos de montagem em versões recentes do PostgreSQL.

    Manipulação de Dados (SQL)

        Padronização de nomenclatura de objetos em snake_case.
        Diferenciação entre filtros de linha (WHERE) e filtros de agregação (HAVING).
        Uso de Window Functions (ROW_NUMBER() OVER) para criação de rankings.
        Implementação de CTEs (Common Table Expressions) para garantir a legibilidade e manutenção de queries complexas.

    Qualidade de Dados & Troubleshooting

        Correção de Tipagem: Identificação e resolução do erro de importação [22P02], onde colunas de texto foram interpretadas como tipo int.
        Solução via mapeamento manual no DBeaver para o tipo TEXT/VARCHAR.
        Saneamento de registros duplicados e identificação de inconsistências em colunas de capacidade.

Rotina de Refatoração e Resiliência
Para garantir a maestria técnica e a confiabilidade da infraestrutura, adoto uma rotina diária de:

    Reconstrução do Ambiente: Exclusão e recriação dos containers e volumes para validar a idempotência da infraestrutura.
    Data Drill-down: Repetição manual de queries de agregação e métricas complexas para consolidar a lógica de negócio.
    Validação de Conexões: Reconfiguração do DBeaver do zero para dominar o mapeamento de drivers e schemas.

Foco atual: Finalizando fundamentos de SQL e preparando para automação com Python
