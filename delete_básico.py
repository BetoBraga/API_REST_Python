import requests
import json

# API criada com o tw-dev-server - Endpoint: http://localhost:3002/api/todo

# Exemplo de GET
def deletar_dados(id):
    requests.delete(f"http://localhost:3002/api/todo?id={id}")

# Chama o método deletar dados
deletar_dados("IbJ6BzCktZKdsXbj")