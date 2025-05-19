from fastapi import APIRouter, Depends
from api.db.mongo import get_db
import random

router = APIRouter()

@router.get("/estimulo")
async def get_estimulo(db=Depends(get_db)):
    collection = db["estimulos"]
    count = await collection.count_documents({})
    if count == 0:
        return {"mensagem": "Nenhum estímulo disponível no banco de dados."}
    random_index = random.randint(0, count - 1)
    cursor = collection.find().skip(random_index).limit(1)
    doc = await cursor.to_list(length=1)
    return {"mensagem": doc[0]["mensagem"]}
