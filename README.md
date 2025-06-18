# 🤖 Painel DilsBot Web — Interface de Automação Total

Este projeto é uma versão com **interface web futurista** do sistema DilsBot, onde comandos ativadores secretos disparam automações de desenvolvimento, deploys, empacotamento e muito mais.

---

## 🎯 Objetivo

Transformar o terminal do dev em uma central de controle interativa com botões que disparam:

- Scripts locais
- Conexões com servidor
- Empacotamento de projetos
- Deploys para nuvem
- E futuramente, comandos de voz e integração com IA

---

## 🚀 Funcionalidades

- ✅ Interface Web (FastAPI + HTML + Tailwind)
- ✅ Comandos ativadores secretos
- ✅ Backend FastAPI conectado
- ✅ Pronto para deploy
- 🔜 Comandos por voz
- 🔜 Integração com IA real

---

## 🧩 Interface

| Código | Comando Secreto                             |
|--------|---------------------------------------------|
| 1      | Libera o foguete da automação               |
| 2      | Chama o servidor Deployer                   |
| 3      | Subir o DilsBot na nuvem                    |
| 4      | Escalar o N8n                               |
| 5      | Conexão VULTR                               |
| 6      | Dia D da Nuvem                              |

---

## ▶️ Como executar localmente

1. Clone o projeto:

```bash
git clone https://github.com/dilson123-tech/painel-dilsbot-web.git
cd painel-dilsbot-web

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


bash
Copiar
Editar
uvicorn app.main:app --reload
Acesse em: http://localhost:8000

✨ Futuro
Adição de comandos por voz

Deploy em Railway ou VULTR

Painel de administração com autenticação

IA integrada para geração de código ou automações

🧠 Criado por
Dilson Pereira — O Professor DilsBot™
GitHub: @dilson123-tech