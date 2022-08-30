import requests
import json

# API criada com o tw-dev-server - Endpoint: http://localhost:3002/api/todo

# Exemplo de GET
def buscar_dados():
    request = requests.get("http://localhost:3002/api/todo")
    todos = json.loads(request.content)
    print(todos)

    # Retorna o index 0 de "nome"
    print(todos[0]['nome'])



buscar_dados()