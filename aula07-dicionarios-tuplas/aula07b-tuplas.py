t = ('a', 'b', 'c', 'd')
print(type(t))

t1 = 'a',
print(t1)

t = tuple("fiap")
print(t[1:])

# ATRIBUIÇÃO DE TUPLAS
a = 5
b = 10
print(f"a: {a}, b: {b}")

a, b = b, a
print(f"a: {a}, b: {b}")

email = "fulano@gmail.com"
usuario, dominio = email.split("@")

print(usuario)
print(dominio)