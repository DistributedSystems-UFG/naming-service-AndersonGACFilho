import grpc
import name_resolution_pb2
import name_resolution_pb2_grpc
import const
import socket

def register(service_name, endpoint):
    # Estabelece uma conexão insegura (sem criptografia) com o servidor gRPC
    with grpc.insecure_channel(const.GRPC_SERVER_ADDRESS+':'+str(const.GRPC_SERVER_PORT)) as channel:
        # Cria um objeto "stub" para chamar os métodos do serviço
        stub = name_resolution_pb2_grpc.NameResolutionStub(channel)
        # Chama o método Register do serviço de resolução de nomes
        response = stub.Register(name_resolution_pb2.ServiceInfo(service_name=service_name, endpoint=endpoint))
        # Exibe a mensagem de resposta do servidor
        print(response.message)

def lookup(service_name):
    # Estabelece uma conexão insegura (sem criptografia) com o servidor gRPC
    with grpc.insecure_channel(const.GRPC_SERVER_ADDRESS+':'+str(const.GRPC_SERVER_PORT)) as channel:
        # Cria um objeto "stub" para chamar os métodos do serviço
        stub = name_resolution_pb2_grpc.NameResolutionStub(channel)
        # Chama o método Lookup do serviço de resolução de nomes
        response = stub.Lookup(name_resolution_pb2.ServiceName(service_name=service_name))
        # Exibe o endpoint associado ao nome do serviço
        print(f'Endpoint para {service_name}: {response.endpoint}')

def unregister(service_name):
    # Estabelece uma conexão insegura (sem criptografia) com o servidor gRPC
    with grpc.insecure_channel(const.GRPC_SERVER_ADDRESS+':'+str(const.GRPC_SERVER_PORT)) as channel:
        # Cria um objeto "stub" para chamar os métodos do serviço
        stub = name_resolution_pb2_grpc.NameResolutionStub(channel)
        # Chama o método Unregister do serviço de resolução de nomes
        response = stub.Unregister(name_resolution_pb2.ServiceName(service_name=service_name))
        # Exibe a mensagem de resposta do servidor
        print(response.message)

def all_services():
    # Estabelece uma conexão insegura (sem criptografia) com o servidor gRPC
    with grpc.insecure_channel(const.GRPC_SERVER_ADDRESS+':'+str(const.GRPC_SERVER_PORT)) as channel:
        # Cria um objeto "stub" para chamar os métodos do serviço
        stub = name_resolution_pb2_grpc.NameResolutionStub(channel)
        # Chama o método AllServices do serviço de resolução de nomes
        response = stub.AllServices(name_resolution_pb2.Empty())
        # Exibe a lista de serviços registrados
        print(f'Serviços registrados: {response.services}')
