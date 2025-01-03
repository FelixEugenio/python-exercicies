import xmlrpc.client

# Função que conecta ao servidor e solicita os parâmetros do usuário
def conectar_ao_servidor():
    server = xmlrpc.client.ServerProxy('http://localhost:8000/RPC2')

    # Solicitar ao usuário o texto para calcular o hash SHA-1
    texto = input("Digite o texto para calcular o hash SHA-1: ")

    # Chamar a função SH1 no servidor
    resultado = server.SH1(texto)

    # Exibir o hash calculado
    print(f"O hash SHA-1 de '{texto}' é: {resultado}")

if __name__ == "__main__":
    conectar_ao_servidor()
