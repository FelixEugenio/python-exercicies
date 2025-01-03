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

# Função para calcular o Mínimo Múltiplo Comum (MMC)
def mmc(a, b):
    return abs(a * b) // mdc(a, b)

# Criar o servidor
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Registrar funções

    server.register_function(mmc, 'mmc')  # Registrar a função mmc


    # Rodar o servidor
    print("Servidor rodando...")
    server.serve_forever()
