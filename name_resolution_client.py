import grpc
import name_resolution_pb2
import name_resolution_pb2_grpc
import const
import socket
import name_resolution_functions

if __name__ == '__main__':
    # Exemplo de uso
    while True:
        # Limpa a tela
        cls = lambda: print('\n'*100)
        # Mostra o menu
        print('Menu')
        print('1 - Registrar serviço')
        print('2 - Consultar serviço')
        print('3 - Desregistrar serviço')
        print('4 - Obter todos os serviços')
        print('5 - Sair')
        option = input('Digite uma opção: ')
        if option == '1':
            service_name = input('Digite o nome do serviço: ')
            endpoint = input('Digite o endpoint do serviço: ')
            # Registra o serviço
            name_resolution_functions.register(service_name, endpoint)
        elif option == '2':
            service_name = input('Digite o nome do serviço: ')
            # Consulta o serviço
            name_resolution_functions.lookup(service_name)
        elif option == '3':
            service_name = input('Digite o nome do serviço: ')
            # Desregistra o serviço
            name_resolution_functions.unregister(service_name)
        elif option == '4':
            # Obtém todos os serviços
            name_resolution_functions.all_services()
        elif option == '5':
            break
        else:
            print('Opção inválida')
        print()

