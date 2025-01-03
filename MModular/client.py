import xmlrpc.client

# Função que conecta ao servidor e solicita os parâmetros do usuário
def conectar_ao_servidor():
    server = xmlrpc.client.ServerProxy('http://localhost:8000/RPC2')

    # Solicitar os três parâmetros ao usuário
    x = int(input("Digite o valor de x: "))
    y = int(input("Digite o valor de y: "))
    n = int(input("Digite o valor de n: "))

    # Chamar a função MModular no servidor
    resultado = server.MModular(x, y, n)

    # Exibir o resultado
    print(f"O resultado de (x * y) % n é: {resultado}")

if __name__ == "__main__":
    conectar_ao_servidor()
