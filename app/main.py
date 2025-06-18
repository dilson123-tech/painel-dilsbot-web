from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.comandos import executar_comando
import os

app = FastAPI()
print("🧠 FastAPI rodando no diretório:", os.getcwd())  # debug

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def painel(request: Request):
    print("✅ Rota '/' acessada")  # debug
    return templates.TemplateResponse("index.html", {"request": request})
