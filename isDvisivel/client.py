import xmlrpc.client


# Conectar ao servidor
def conectar_ao_servidor():
    server = xmlrpc.client.ServerProxy('http://localhost:8000/RPC2')

    # Solicitar os valores ao usuário
    x = int(input("Digite o primeiro valor (x): "))
    y = int(input("Digite o segundo valor (y): "))

    # Chamar a função isDivisivel no servidor
    resultado = server.isDivisivel(x, y)

    # Exibir o resultado
    if resultado == True:
        print(f"{x} é divisível por {y}.")
    elif resultado == False:
        print(f"{x} não é divisível por {y}.")
    else:
        print(resultado)  # Caso seja erro, como divisão por zero.


if __name__ == "__main__":
    conectar_ao_servidor()
