from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_get_estimulo():
    response = client.get("/estimulo")
    assert response.status_code == 200

def test_post_estimulo():
    payload = {
        "mensagem": "Teste via Pytest",
        "tipo": "texto"
    }
    response = client.post("/estimulo", json=payload)
    assert response.status_code == 200
    assert response.json()["mensagem"] == payload["mensagem"]

def test_delete_estimulo():
    payload = {"mensagem": "Para deletar", "tipo": "texto"}
    post_response = client.post("/estimulo", json=payload)
    id = post_response.json()["id"]

    delete_response = client.delete(f"/estimulo/{id}")
    assert delete_response.status_code == 204

    get_response = client.get("/estimulos")
    ids = [r["id"] for r in get_response.json()]
    assert id not in ids

def test_put_estimulo():
    payload = {"mensagem": "Antes do update", "tipo": "texto"}
    post_response = client.post("/estimulo", json=payload)
    id = post_response.json()["id"]

    update_payload = {"mensagem": "Depois do update"}
    put_response = client.put(f"/estimulo/{id}", json=update_payload)
    assert put_response.status_code == 200

    get_all = client.get("/estimulos")
    dados = [doc for doc in get_all.json() if doc["id"] == id]
    assert dados[0]["mensagem"] == "Depois do update"

def test_delete_invalid_id():
    response = client.delete("/estimulo/invalid-id-123")
    assert response.status_code == 400
    assert response.json()["detail"] == "ID inválido"
