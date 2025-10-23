from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI()

# Rota raiz
@app.get("/")
def read_root():
    return {"message": "API rodando!"}

# Rota para posts
@app.get("/posts/{framework}")
def read_posts(framework: str):
    return {
        "posts": [
            {"title": f"Criando uma aplicação com {framework}", "date": datetime.now(timezone.utc)},
            {"title": f"Dominando FastAPI com {framework}", "date": datetime.now(timezone.utc)}
        ]
    }
