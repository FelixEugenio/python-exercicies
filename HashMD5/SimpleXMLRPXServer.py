import hashlib
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


# Restrição para um caminho específico
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Função para calcular o hash MD5
def MD5(x):
    # Cria o objeto MD5
    hash_object = hashlib.md5()

    # Atualiza o objeto hash com a string convertida para bytes
    hash_object.update(x.encode('utf-8'))

    # Retorna o valor hexadecimal do hash
    return hash_object.hexdigest()


# Criar o servidor
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Registrar a função MD5 no servidor
    server.register_function(MD5, 'MD5')

    print("Servidor rodando em http://localhost:8000")
    server.serve_forever()
