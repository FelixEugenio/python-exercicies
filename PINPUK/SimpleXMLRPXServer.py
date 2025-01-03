import random
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrição para um caminho específico
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Função para gerar PIN ou PUK
def gerarPinPuk(x):
    if x == 0:
        # Gerar um PIN de 4 dígitos
        return random.randint(1000, 9999)
    elif x == 1:
        # Gerar um PUK de 8 dígitos
        return random.randint(10000000, 99999999)
    else:
        return "Valor inválido. Envie 0 para PIN ou 1 para PUK."

# Criar o servidor
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Registrar a função gerarPinPuk no servidor
    server.register_function(gerarPinPuk, 'gerarPinPuk')

    print("Servidor rodando em http://localhost:8000")
    server.serve_forever()
