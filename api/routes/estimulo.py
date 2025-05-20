from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, Query, status
from api.db.mongo import get_db
import random

class Estimulo(BaseModel):
    mensagem: str = Field(..., min_length=1)
    tipo: Optional[str] = "texto"

class EstimuloAtualizacao(BaseModel):
    mensagem: Optional[str]
    tipo: Optional[str]

router = APIRouter()

@router.get("/estimulo")
async def get_estimulo(tipo: Optional[str] = Query(default=None), db=Depends(get_db)):
    collection = db["estimulos"]
    
    # Cria filtro se tipo for informado
    filtro = {"tipo": tipo} if tipo else {}

    count = await collection.count_documents(filtro)
    if count == 0:
        return {"mensagem": "Nenhum estímulo disponível com esse filtro."}
    
    random_index = random.randint(0, count - 1)
    cursor = collection.find(filtro).skip(random_index).limit(1)
    doc = await cursor.to_list(length=1)
    
    return {"mensagem": doc[0]["mensagem"]}

@router.post("/estimulo")
async def criar_estimulo(est: Estimulo, db=Depends(get_db)):
    collection = db["estimulos"]
    result = await collection.insert_one(est.model_dump())  # ✅ compatível com Pydantic v2
    return {"id": str(result.inserted_id), "mensagem": est.mensagem}

@router.get("/estimulos")
async def listar_estimulos(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db=Depends(get_db)
):
    collection = db["estimulos"]
    cursor = collection.find().skip(skip).limit(limit)
    documentos = await cursor.to_list(length=limit)

    resultado = [
        {
            "id": str(doc["_id"]),
            "mensagem": doc.get("mensagem", ""),
            "tipo": doc.get("tipo", "")
        }
        for doc in documentos
    ]
    return resultado

@router.delete("/estimulo/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_estimulo(id: str, db=Depends(get_db)):
    collection = db["estimulos"]

    # Verifica se o ID é válido
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID inválido")

    result = await collection.delete_one({"_id": ObjectId(id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Estímulo não encontrado")
    
@router.put("/estimulo/{id}")
async def atualizar_estimulo(id: str, dados: EstimuloAtualizacao, db=Depends(get_db)):
    collection = db["estimulos"]

    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID inválido")

    atualizacao = {k: v for k, v in dados.dict().items() if v is not None}

    if not atualizacao:
        raise HTTPException(status_code=400, detail="Nenhum dado para atualizar.")

    result = await collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": atualizacao}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Estímulo não encontrado.")

    return {"mensagem": "Estímulo atualizado com sucesso."}