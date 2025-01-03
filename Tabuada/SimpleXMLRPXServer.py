from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrição para um caminho específico
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Função que calcula a tabuada de x
def tabuada(x):
    return [x * i for i in range(1, 11)]

# Criar o servidor
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Registrar a função tabuada no servidor
    server.register_function(tabuada, 'tabuada')

    print("Servidor rodando em http://localhost:8000")
    server.serve_forever()
