import requests
import json
import post_básico_class

# Exemplo de GET
def buscar_dados():
    request = requests.get("http://localhost:3002/api/todo")
    todos = json.loads(request.content)
    print(todos) # Retorna todo o conteúdo do JSON

    print(todos[0]['nome']) # Retorna o index 0 de "nome"


# Exemplo de POST em REST API
def cadastrar_dados(post_básico_class):
    requests.post("http://localhost:3002/api/todo",
                  data=json.dumps(post_básico_class.__dict__)) # Converte JSON & Dicionário (Aqui o JSON é o import)

# Argumentos desse método devem ser, em ordem, os atributos a serem adicionados 
# nomedométodo(nomedoimport.Nomedaclasse("id", "titulo", "nome"))
cadastrar_dados(post_básico_class.Post_básico_class("Erik", "Borges", "Javascript", "Emprego"))

# GET 
buscar_dados()
