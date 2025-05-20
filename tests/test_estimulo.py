import pytest
from httpx import AsyncClient
from api.main import app

@pytest.mark.asyncio
async def test_get_estimulo():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/estimulo")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_post_estimulo():
    payload = {
        "mensagem": "Teste via Pytest",
        "tipo": "texto"
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/estimulo", json=payload)
    assert response.status_code == 200
    assert response.json()["mensagem"] == payload["mensagem"]

@pytest.mark.asyncio
async def test_delete_estimulo():
    # Cria um estímulo para ser deletado
    payload = {"mensagem": "Para deletar", "tipo": "texto"}
    async with AsyncClient(app=app, base_url="http://test") as ac:
        post_response = await ac.post("/estimulo", json=payload)
        id = post_response.json()["id"]

        # Agora deleta
        delete_response = await ac.delete(f"/estimulo/{id}")
        assert delete_response.status_code == 204

        # Verifica se realmente foi deletado
        get_response = await ac.get(f"/estimulo?tipo=texto")
        ids = [r["id"] for r in await ac.get("/estimulos").then(lambda r: r.json())]
        assert id not in ids

@pytest.mark.asyncio
async def test_put_estimulo():
    # Cria estímulo
    payload = {"mensagem": "Antes do update", "tipo": "texto"}
    async with AsyncClient(app=app, base_url="http://test") as ac:
        post_response = await ac.post("/estimulo", json=payload)
        id = post_response.json()["id"]

        # Atualiza
        update_payload = {"mensagem": "Depois do update"}
        put_response = await ac.put(f"/estimulo/{id}", json=update_payload)
        assert put_response.status_code == 200

        # Busca para confirmar atualização
        get_all = await ac.get("/estimulos")
        dados = [doc for doc in get_all.json() if doc["id"] == id]
        assert dados[0]["mensagem"] == "Depois do update"

@pytest.mark.asyncio
async def test_delete_invalid_id():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.delete("/estimulo/invalid-id-123")
        assert response.status_code == 400
        assert response.json()["detail"] == "ID inválido"