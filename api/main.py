from fastapi import FastAPI
from api.routes import estimulo

app = FastAPI()

app.include_router(estimulo.router)