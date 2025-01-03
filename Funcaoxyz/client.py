import xmlrpc.client

# Função que conecta ao servidor e solicita os parâmetros do usuário
def conectar_ao_servidor():
    server = xmlrpc.client.ServerProxy('http://localhost:8000/RPC2')

    # Solicitar ao usuário a operação a ser realizada
    x = input("Digite a operação (exponencial, log): ")
    y = float(input("Digite o valor de y (base ou base para logaritmo): "))
    z = float(input("Digite o valor de z (expoente ou argumento para logaritmo): "))

    try:
        # Chamar a função f no servidor com os parâmetros fornecidos
        resultado = server.f(x, y, z)

        # Exibir o resultado
        print(f"Resultado da operação {x}({y}, {z}): {resultado}")

    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    conectar_ao_servidor()
