import pandas as pd
from sqlalchemy import create_engine
import logging
import os
from dotenv import load_dotenv

# Configura onde o log será salvo (na pasta logs)
os.makedirs('logs', exist_ok=True)
logging.basicConfig(
    filename='logs/ingestion.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a' # 'a' de append: adiciona ao fim do arquivo sem apagar o anterior
)

# Exemplo de como usar:
logging.info("Iniciando processo de ingestão...")

load_dotenv(os.path.join('infra', '.env'))

# 1. Configurações de Conexão usando os nomes alocados no .env
DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")
DB_DB   = os.getenv("POSTGRES_DB")
DB_HOST = "localhost"
DB_PORT = "5432"

# Criando a conexão com o banco
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_DB}")

def run_ingestion():
    file_path = os.path.join("data", "raw", "Leitos_2025.csv")
    
    logging.info(f"Iniciando leitura do arquivo: {file_path}")
    
    try:
        # 3. Leitura do CSV
        df = pd.read_csv(file_path, sep=';', encoding='latin1', low_memory=False)
        
        msg_sucesso_leitura = f"Arquivo lido com sucesso! Linhas encontradas: {len(df)}"
        print(f"✅ {msg_sucesso_leitura}")
        logging.info(msg_sucesso_leitura)
        
        # 4. Limpeza Básica de Colunas
        df.columns = [c.lower().replace(' ', '_').replace('.', '') for c in df.columns]
        
        # 5. Carga para o Postgres
        print("🚀 Enviando dados para o banco Docker...")
        df.to_sql('raw_leitos', engine, if_exists='replace', index=False)
        
        msg_final = "🎉 SUCESSO! A tabela 'raw_leitos' foi criada e populada."
        print(msg_final)
        logging.info("Carga para o banco de dados finalizada com sucesso.")

    except Exception as e:
        erro_msg = f"ERRO na ingestão: {e}"
        print(f"❌ {erro_msg}")
        logging.error(erro_msg) # Aqui o erro é gravado no arquivo logs/ingestion.log

if __name__ == "__main__":
    run_ingestion()