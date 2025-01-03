from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrição para um caminho específico
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Função que calcula o resto da divisão de (x * y) por n
def MModular(x, y, n):
    if n == 0:
        return "Erro: Divisão por zero não permitida."  # Prevenção de divisão por zero
    return (x * y) % n

# Criar o servidor
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Registrar a função MModular no servidor
    server.register_function(MModular, 'MModular')

    print("Servidor rodando em http://localhost:8000")
    server.serve_forever()
