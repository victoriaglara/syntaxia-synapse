import json
from pymongo import MongoClient

# Conecte ao MongoDB local
client = MongoClient("mongodb://mongo:27017")
db = client["syntaxia"]
colecao = db["estimulos"]

# Carrega os dados do arquivo
with open("api/db/seed.json", encoding="utf-8") as f:
    dados = json.load(f)

# Insere no banco
colecao.insert_many(dados)

print(f"Inseridos {len(dados)} estímulos no MongoDB!")