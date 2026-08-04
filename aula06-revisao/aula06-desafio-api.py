endpoints = ["/login", "/produtos", "/pedidos"]

status = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500]
]

# print(endpoints[0])
# print(status[0][2])

# Função para detectar se UM status é sucesso

def eh_sucesso(codigo):
     return codigo >= 200 and codigo <= 299

print(eh_sucesso(status[2][1]))

# status[0] = [200, 200, 401, 200, 500] --> False
# status[2] = [201, 500, 502, 201, 500] --> True