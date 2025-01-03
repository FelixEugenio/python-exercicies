from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrição para um caminho específico
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Função que verifica se x é divisível por y
def isDivisivel(x, y):
    # Verifica se x é divisível por y
    if y == 0:
        return "Erro: Divisão por zero não permitida."
    return x % y == 0

# Criar o servidor
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Registrar a função isDivisivel no servidor
    server.register_function(isDivisivel, 'isDivisivel')

    print("Servidor rodando em http://localhost:8000")
    server.serve_forever()
