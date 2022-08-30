import requests
import json

# API criada com o tw-dev-server - Endpoint: http://localhost:3002/api/todo

# Exemplo de GET
def buscar_dados_id(id):
   
    request = requests.get(f"http://localhost:3002/api/todo?id={id}")  # fstring para a str no endpoint
    todo = json.loads(request.content)
    print(todo)
    # Retorna título do ID
    print(todo['titulo'])



buscar_dados_id("h7i39LVliST6r8kI")