import math
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrição para um caminho específico
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Função para calcular inversas trigonométricas
def inv_trignometria(x, y):
    # Verifica a função inversa a ser calculada
    if x == 'acos':
        if -1 <= y <= 1:  # Verifica se y está no intervalo válido para acos
            return math.acos(y)
        else:
            raise ValueError("O valor de y para 'acos' deve estar entre -1 e 1.")
    elif x == 'asin':
        if -1 <= y <= 1:  # Verifica se y está no intervalo válido para asin
            return math.asin(y)
        else:
            raise ValueError("O valor de y para 'asin' deve estar entre -1 e 1.")
    elif x == 'atg':
        return math.atan(y)
    else:
        raise ValueError("Função inversa inválida. Use 'acos', 'asin' ou 'atg'.")

# Criar o servidor
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Registrar a função inv_trignometria no servidor
    server.register_function(inv_trignometria, 'inv_trignometria')

    print("Servidor rodando em http://localhost:8000")
    server.serve_forever()
