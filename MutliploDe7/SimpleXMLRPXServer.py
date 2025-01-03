from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Função para verificar se o número é múltiplo de 7
def isMultiplo7(x):
    return x % 7 == 0

# Função para somar dois números
def adder_function(x, y):
    return x + y

# Função para multiplicar dois números (em uma classe)
class MyFuncs:
    def mul(self, x, y):
        return x * y

# Criar o servidor
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Registrar funções padrão
    server.register_function(pow)  # A função pow() já está registrada automaticamente
    server.register_function(adder_function, 'add')  # Função de soma
    server.register_function(isMultiplo7, 'isMultiplo7')  # Função de múltiplo de 7

    # Registrar a classe MyFuncs que contém a função 'mul'
    server.register_instance(MyFuncs())

    # Rodar o servidor
    print("Servidor rodando em http://localhost:8000")
    server.serve_forever()
