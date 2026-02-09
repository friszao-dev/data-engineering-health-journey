import pandas as pd
from sqlalchemy import create_engine

# Configurações de conexão (devem bater com seu docker-compose.yml)
DB_USER = 'admin'
DB_PASS = 'minhasenha123'
DB_HOST = 'localhost' # Usamos localhost porque o Python está fora do Docker
DB_PORT = '5432'
DB_NAME = 'db_saude'

# 1. Cria a engine de conexão
conn_string = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(conn_string)

try:
    # 2. Teste Simples: Criar um DataFrame de exemplo
    df_teste = pd.DataFrame({'status': ['Conexão Python-Postgres OK!']})
    
    # 3. Enviar para o banco
    df_teste.to_sql('teste_python', engine, if_exists='replace', index=False)
    print("🚀 Sucesso! O Python conseguiu gravar dados no seu banco Docker.")
except Exception as e:
    print(f"❌ Erro na conexão: {e}")