
Este repositório documenta minha transição de carreira para Engenharia de Dados, focando na análise de dados públicos de saúde do Brasil (DATASUS).

# Infraestrutura
Para este projeto, utilizei o Docker para subir uma instância de PostgreSQL, garantindo um ambiente isolado e replicável.


# Comando utilizado para subir o container
docker run --name postgres-saude `
  -e POSTGRES_PASSWORD=minhasenha123 `
  -p 5432:5432 `
  -d postgres