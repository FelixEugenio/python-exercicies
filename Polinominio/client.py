import xmlrpc.client


# Conectar ao servidor
def conectar_ao_servidor():
    server = xmlrpc.client.ServerProxy('http://localhost:8000/RPC2')

    # Solicitar os parâmetros ao usuário
    x = float(input("Digite o valor de x: "))
    k = int(input("Digite o grau do polinômio (k): "))

    # Chamar a função polinomio no servidor
    resultado = server.polinomio(k, x)

    # Exibir o resultado
    print(f"O valor do polinômio para x = {x} e grau k = {k} é: {resultado}")


if __name__ == "__main__":
    conectar_ao_servidor()
