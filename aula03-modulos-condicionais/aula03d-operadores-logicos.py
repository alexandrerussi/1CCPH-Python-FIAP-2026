# LOGICA E (and)

verifica_email = True
verifica_senha = False

verifica_login = verifica_email and verifica_senha
print(verifica_login)

if verifica_login:
    print("Entrar no programa")

# LOGICA OU (or)
logica_ou = True or False or False
print(logica_ou)

# OPERADOR NOT
negacao = not True
print(negacao)

if not verifica_login:
    print("loga certo ai cara")