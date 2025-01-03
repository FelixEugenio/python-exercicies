import xmlrpc.client

# Conectar ao servidor
s = xmlrpc.client.ServerProxy('http://localhost:8000/RPC2')

# Entradas do usuário
x = int(input("entre o 1-valor: "))
y = int(input("entre o 2-valor: "))

# Chamar as funções
print("MMC de", x, "e", y, "é:", s.mmc(x, y))  # Chama a função mmc

