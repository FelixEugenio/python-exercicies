import hashlib
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


# Restrição para um caminho específico
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Função para calcular o hash SHA-1
def SH1(x):
    # Cria o objeto SHA-1
    hash_object = hashlib.sha1()

    # Atualiza o objeto hash com a string convertida para bytes
    hash_object.update(x.encode('utf-8'))

    # Retorna o valor hexadecimal do hash
    return hash_object.hexdigest()


# Criar o servidor
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Registrar a função SH1 no servidor
    server.register_function(SH1, 'SH1')

    print("Servidor rodando em http://localhost:8000")
    server.serve_forever()
