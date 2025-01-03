import xmlrpc.client

# Função que conecta ao servidor e solicita os parâmetros do usuário
def conectar_ao_servidor():
    server = xmlrpc.client.ServerProxy('http://localhost:8000/RPC2')

    # Solicitar ao usuário a função trigonométrica e o argumento
    x = input("Digite a função trigonométrica (cos, sin, tg): ")
    y = float(input("Digite o argumento em graus: "))

    # Chamar a função trignometria no servidor
    resultado = server.trignometria(x, y)

    # Exibir o resultado
    print(f"O valor de {x}({y} graus) é: {resultado}")

if __name__ == "__main__":
    conectar_ao_servidor()
