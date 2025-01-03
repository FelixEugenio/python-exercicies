from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrição para um caminho específico
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Função que calcula o polinômio 1 + 2x + 3x^2 + ... + (k+1)x^k
def polinomio(k, x):
    result = 0
    for i in range(k + 1):
        result += (i + 1) * (x ** i)
    return result

# Criar o servidor
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Registrar a função 'polinomio' no servidor
    server.register_function(polinomio, 'polinomio')

    print("Servidor rodando em http://localhost:8000")
    server.serve_forever()
