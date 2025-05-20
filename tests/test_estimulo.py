import pytest
from httpx import AsyncClient, ASGITransport
from api.main import app

@pytest.mark.asyncio
async def test_get_estimulo():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/estimulo")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_post_estimulo():
    payload = {"mensagem": "Teste via Pytest", "tipo": "texto"}
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/estimulo", json=payload)
    assert response.status_code == 200
    assert "id" in response.json()

@pytest.mark.asyncio
async def test_delete_estimulo():
    payload = {"mensagem": "Para deletar", "tipo": "texto"}
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        post_response = await ac.post("/estimulo", json=payload)
        id = post_response.json()["id"]

        delete_response = await ac.delete(f"/estimulo/{id}")
        assert delete_response.status_code == 204

@pytest.mark.asyncio
async def test_put_estimulo():
    payload = {"mensagem": "Antes do update", "tipo": "texto"}
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        post_response = await ac.post("/estimulo", json=payload)
        id = post_response.json()["id"]

        update_payload = {"mensagem": "Depois do update"}
        put_response = await ac.put(f"/estimulo/{id}", json=update_payload)
        assert put_response.status_code == 200

@pytest.mark.asyncio
async def test_delete_invalid_id():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.delete("/estimulo/invalid-id-123")
        assert response.status_code == 400
