import grpc
import name_resolution_pb2  # Importa as mensagens protobuf geradas
import name_resolution_pb2_grpc  # Importa o serviço gRPC gerado
from concurrent import futures
import time
import const

_last_service_number = 0

# Implementação do serviço gRPC
class NameResolutionServicer(name_resolution_pb2_grpc.NameResolutionServicer):
    def __init__(self):
        # Dicionário para armazenar registros de serviços (mapeamento de nome para endpoint)
        self.service_registry = {}

    def Register(self, request, context):
        # Manipulador para a chamada RPC de Registro
        # Registra um serviço com um determinado nome e endpoint
        self.service_registry[request.service_name] = request.endpoint
        print(f'Registrando serviço {request.service_name} com endpoint {request.endpoint}')
        print(f'Número de serviços registrados: {len(self.service_registry)}')
        print(f'Serviços registrados: {self.service_registry}')
        return name_resolution_pb2.Result(message=f'Serviço {request.service_name} registrado com sucesso')

    def Lookup(self, request, context):
        # Manipulador para a chamada RPC de Consulta
        # Procura o endpoint de um determinado nome de serviço
        if request.service_name in self.service_registry:
            return name_resolution_pb2.Endpoint(endpoint=self.service_registry[request.service_name])
        else:
            return name_resolution_pb2.Endpoint(endpoint='Serviço não encontrado')

    def Unregister(self, request, context):
        # Manipulador para a chamada RPC de Desregistro
        # Desregistra um serviço com um determinado nome
        if request.service_name in self.service_registry:
            del self.service_registry[request.service_name]
            return name_resolution_pb2.Result(message=f'Serviço {request.service_name} desregistrado com sucesso')
        else:
            return name_resolution_pb2.Result(message='Serviço não encontrado')
        
    def AllServices(self, request, context):
        # Manipulador para a chamada RPC de Obter Todos os Serviços
        # Retorna uma lista de todos os serviços registrados
        
        # Cria uma lista dos nomes de serviço registrados
        registered_services = ', '.join(list(self.service_registry.keys()))
        
        # Retorna a lista de serviços no formato apropriado
        return name_resolution_pb2.Services(services=registered_services)

# Função para iniciar o servidor gRPC
def serve():
    # Cria um servidor gRPC com um pool de threads
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # Adiciona o NameResolutionServicer ao servidor
    name_resolution_pb2_grpc.add_NameResolutionServicer_to_server(NameResolutionServicer(), server)
    
    # Liga o servidor para ouvir na porta 50051
    server.add_insecure_port('[::]:'+str(const.GRPC_SERVER_PORT))
    
    # Inicia o servidor
    server.start()
    
    try:
        # Mantém o servidor em execução até ser interrompido
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        # Interrompe o servidor em caso de interrupção do teclado
        server.stop(0)

# Ponto de entrada quando o script é executado
if __name__ == '__main__':
    # Chama a função serve para iniciar o servidor
    serve()
