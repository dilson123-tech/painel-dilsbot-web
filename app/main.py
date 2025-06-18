from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def get_painel():
    return FileResponse("static/index.html")

@app.post("/comando/{codigo}")
def executar_comando(codigo: str):
    comandos = {
        "foguete": "🚀 Foguete liberado com sucesso!",
        "deployer": "🛠️ Deployer ativado!",
        "nuvem": "☁️ Subida para a nuvem iniciada!",
        "n8n": "📡 N8n escalado com sucesso!",
        "vultr": "🔗 Conexão com VULTR estabelecida!",
        "diaD": "🎯 Operação Dia D da Nuvem executada!"
    }
    return {"mensagem": comandos.get(codigo, "❌ Código não reconhecido")}
