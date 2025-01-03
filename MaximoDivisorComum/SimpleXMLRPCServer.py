from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Função para calcular o Máximo Divisor Comum (MDC)
def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Criar o servidor
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Registrar funções

    server.register_function(mdc, 'mdc')  # Registrar a função mdc


    # Rodar o servidor
    print("Servidor rodando...")
    server.serve_forever()
