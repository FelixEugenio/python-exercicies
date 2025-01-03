import xmlrpc.client

# Conectar ao servidor
s = xmlrpc.client.ServerProxy('http://localhost:8000/RPC2')

# Entradas do usuário
x = int(input("entre o 1-valor: "))
y = int(input("entre o 2-valor: "))

# Chamar as funções
print("MDC de", x, "e", y, "é:", s.mdc(x, y))  # Chama a função mdc

