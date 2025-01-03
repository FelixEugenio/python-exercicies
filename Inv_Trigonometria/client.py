import xmlrpc.client

# Função que conecta ao servidor e solicita os parâmetros do usuário
def conectar_ao_servidor():
    server = xmlrpc.client.ServerProxy('http://localhost:8000/RPC2')

    # Solicitar ao usuário a função inversa e o argumento
    x = input("Digite a função inversa trigonométrica (acos, asin, atg): ")
    y = float(input("Digite o argumento: "))

    try:
        # Chamar a função inv_trignometria no servidor
        resultado = server.inv_trignometria(x, y)

        # Exibir o resultado
        print(f"O valor de {x}({y}) é: {resultado} radianos")

    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    conectar_ao_servidor()
