from fastapi import FastAPI

app = FastAPI()

@app.get("/estimulo")
def get_estimulo():
    return {"mensagem": "Você é capaz. Só precisa dar o primeiro passo."}