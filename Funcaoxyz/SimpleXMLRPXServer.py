import math
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrição para um caminho específico
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Função que realiza a operação exponencial ou logaritmo
def f(x, y, z):
    if x == 'exponencial':
        return y ** z  # Calcula y^z
    elif x == 'log':
        if y <= 0 or y == 1:
            raise ValueError("A base 'y' deve ser maior que 0 e diferente de 1 para o logaritmo.")
        if z <= 0:
            raise ValueError("O argumento 'z' deve ser maior que 0 para o logaritmo.")
        return math.log(z, y)  # Calcula logaritmo de z na base y
    else:
        raise ValueError("Operação inválida. Use 'exponencial' ou 'log'.")

# Criar o servidor
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Registrar a função f no servidor
    server.register_function(f, 'f')

    print("Servidor rodando em http://localhost:8000")
    server.serve_forever()
