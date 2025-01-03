import math
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


# Restrição para um caminho específico
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Função para calcular trigonometria
def trignometria(x, y):
    # Converte o argumento de graus para radianos
    y_radians = math.radians(y)

    # Verifica a função trigonométrica a ser calculada
    if x == 'cos':
        return math.cos(y_radians)
    elif x == 'sin':
        return math.sin(y_radians)
    elif x == 'tg':
        return math.tan(y_radians)
    else:
        raise ValueError("Função trigonométrica inválida. Use 'cos', 'sin' ou 'tg'.")


# Criar o servidor
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Registrar a função trignometria no servidor
    server.register_function(trignometria, 'trignometria')

    print("Servidor rodando em http://localhost:8000")
    server.serve_forever()
