import xmlrpc.client

# Função que conecta ao servidor e solicita os parâmetros do usuário
def conectar_ao_servidor():
    server = xmlrpc.client.ServerProxy('http://localhost:8000/RPC2')

    # Solicitar ao usuário o número para calcular a tabuada
    x = int(input("Digite um número para calcular a sua tabuada: "))

    # Chamar a função tabuada no servidor
    resultado = server.tabuada(x)

    # Exibir o resultado
    print(f"A tabuada de {x} é:")
    for i, res in enumerate(resultado, 1):
        print(f"{x} x {i} = {res}")

if __name__ == "__main__":
    conectar_ao_servidor()
