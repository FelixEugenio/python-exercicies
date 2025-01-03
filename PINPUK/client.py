import xmlrpc.client

# Função que conecta ao servidor e solicita os parâmetros do usuário
def conectar_ao_servidor():
    server = xmlrpc.client.ServerProxy('http://localhost:8000/RPC2')

    # Solicitar ao usuário se ele quer gerar um PIN (0) ou PUK (1)
    escolha = int(input("Digite 0 para gerar um PIN ou 1 para gerar um PUK: "))

    # Chamar a função gerarPinPuk no servidor
    resultado = server.gerarPinPuk(escolha)

    # Exibir o resultado
    print(f"O valor gerado é: {resultado}")

if __name__ == "__main__":
    conectar_ao_servidor()
