# Data Engineering Health Journey - Análise DATASUS

Este repositório documenta toda a minha jornada de transição de carreira para a Engenharia de Dados. O projeto foca na estruturação, tratamento e análise de dados públicos de saúde do Brasil (leitos hospitalares), utilizando tecnologias essenciais do ecossistema de dados.

---

# Tecnologias e Ferramentas #
- Banco de Dados: PostgreSQL (Relacional)
- Infraestrutura: Docker & Docker Desktop
- IDE de Banco de Dados: DBeaver
- Controle de Versão: Git & GitHub

---

-  Etapas do Projeto

1. Configuração do Ambiente (Docker)
A primeira etapa consistiu em isolar o ambiente de banco de dados utilizando containers. Evoluí para o uso de Volumes para garantir a persistência dos dados. Devido à atualização para o PostgreSQL 18+, tive erros de conexão com o banco, identificando que o problema estava no diretório criado anteriormente, o mapeamento foi ajustado para o diretório principal, permitindo que o sistema gerencie subpastas de versão e upgrades de forma nativa.

# Comando para subir o container com persistência de dados (Ajustado para Postgres 18+)

docker run --name postgres-saude `
  -e POSTGRES_PASSWORD=minhasenha123 `
  -p 5432:5432 `
  -v pgdata_saude:/var/lib/postgresql `
  -d postgres

---

- Aprendizados Técnicos

1. Persistência e Infraestrutura:
- Implementação de Docker Volumes para desassociar o ciclo de vida do container dos dados armazenados.
- Resolução de conflitos de montagem (Troubleshooting) em versões recentes do PostgreSQL, movendo o ponto de montagem do volume de /var/lib/postgresql/data para /var/lib/postgresql.

2. Manipulação de Dados (SQL):
- Gerenciamento de Case Sensitivity no PostgreSQL e padronização de nomenclatura de objetos.
- Diferenciação entre filtros de linha (WHERE) e filtros de agregação (HAVING).
- Construção de métricas derivadas e indicadores percentuais para análise de negócio.

3. Qualidade de Dados:
- Uso de técnicas de agrupamento (GROUP BY) para saneamento de registros duplicados e identificação de inconsistências em colunas de capacidade hospitalar.