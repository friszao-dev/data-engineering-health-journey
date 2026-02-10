import pandas as pd
from sqlalchemy import create_engine
import os

# 1. Configurações de Conexão (Ajuste se sua senha for diferente)
DB_USER = "admin"
DB_PASS = "minhasenha123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "db_saude"

# Criando a conexão com o banco
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

def run_ingestion():
    # 2. Caminho do arquivo
    # Usamos caminhos relativos para o projeto funcionar em qualquer PC
    file_path = os.path.join("data", "raw", "Leitos_2025.csv")
    
    print(f"📂 Iniciando leitura do arquivo: {file_path}")
    
    try:
        # 3. Leitura do CSV
        # O SUS geralmente usa 'sep=;' e 'encoding=latin1' ou 'utf-8'
        df = pd.read_csv(file_path, sep=';', encoding='latin1', low_memory=False)
        
        print(f"✅ Arquivo lido com sucesso! Linhas encontradas: {len(df)}")
        
        # 4. Limpeza Básica de Colunas (Lei da Estética)
        # Transforma 'Nome da Coluna' em 'nome_da_coluna'
        df.columns = [c.lower().replace(' ', '_').replace('.', '') for c in df.columns]
        
        # 5. Carga para o Postgres
        print("🚀 Enviando dados para o banco Docker (isso pode levar alguns segundos)...")
        df.to_sql('raw_leitos', engine, if_exists='replace', index=False)
        
        print("🎉 SUCESSO! A tabela 'raw_leitos' foi criada e populada.")

    except Exception as e:
        print(f"❌ ERRO na ingestão: {e}")

if __name__ == "__main__":
    run_ingestion()