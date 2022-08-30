import requests
import json
import post_básico_class

# Exemplo de GET - Retorna 
def buscar_dados():
    request = requests.get("http://localhost:3002/api/todo")
    todos = json.loads(request.content)
    print(todos) # Retorna todo o conteúdo do JSON

    print(todos[0]['nome']) # Retorna o index 0 de "nome"


# Exemplo de PUT em REST API - Edita
def editar_dados(id, post_básico_class):
    requests.put(f"http://localhost:3002/api/todo?id={id}",
                 data=json.dumps(post_básico_class.__dict__))

# Chama o método editar_dados 
editar_dados("WypLz7MHXoI1XegZ", # Filtra por ID [API] 
            post_básico_class.Post_básico_class("Robertinho", "Braguinha", "Pythonzinho", "Estáginho")) # Dados a serem alterados

# GET 
buscar_dados()
