import xmlrpc.client

# Conectar ao servidor
s = xmlrpc.client.ServerProxy('http://localhost:8000')

# Solicitar valores ao usuário
x = int(input("Digite o 1º valor: "))
y = int(input("Digite o 2º valor: "))

# Exibir o tipo de x (para verificar se é inteiro)
print(type(x))

# Chamar as funções do servidor
# Exemplo de potência: x % 150 elevado a y % 10
print(f"Resultado de Multiplo(x % 150, y % 10): {s.isMultiplo7(x)}")

# Exemplo de soma
print(f"Resultado de add(x, y): {s.add(x, y)}")

# Exemplo de multiplicação (em uma classe registrada no servidor)
print(f"Resultado de mul(x, y): {s.mul(x, y)}")

# Listar todos os métodos disponíveis no servidor
print("Métodos disponíveis no servidor:")
print(s.system.listMethods())
