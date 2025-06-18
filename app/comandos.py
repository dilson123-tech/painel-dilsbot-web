import time

def executar_comando(codigo: int):
    comandos = {
        1: "🚀 Foguete da automação liberado!",
        2: "⚙️ Servidor Deployer inicializado!",
        3: "📦 DilsBot empacotado para nuvem!",
        4: "🧩 N8n escalado com sucesso!",
        5: "📡 Conexão com VULTR ativada!",
        6: "🌍 Deploy final executado. DilsBot no ar!",
    }

    time.sleep(1)
    return comandos.get(codigo, "❌ Comando desconhecido.")
