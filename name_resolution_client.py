import grpc
import os
import name_resolution_pb2
import name_resolution_pb2_grpc
import const
import socket
import name_resolution_functions_server
import name_resolution_functions_server2

if __name__ == '__main__':
    while True:
        # Imprime Título
        os.system('cls')
        print('Cliente de Resolução de Nomes')
        print('=============================\n')
        print('Ips e portas')
        # Mostra o IP do cliente	
        print(f'IP do cliente: {socket.gethostbyname(socket.gethostname())}')
        # Mostra IP dos servidores
        print(f'Endereço do servidor 1: {const.GRPC_SERVER_ADDRESS}:{const.GRPC_SERVER_PORT}')
        print(f'Endereço do servidor 2: {const.GRPC_SERVER_ADDRESS2}:{const.GRPC_SERVER_PORT}\n')
        # Mostra o menu de seleção de servidor
        print('\nSelecione o servidor')
        print('1 - Servidor 1')
        print('2 - Servidor 2')
        print('3 - Alterar endereço do servidor')
        print('4 - Sair')
        option = input('\nDigite uma opção: ')
        if option == '1':
            while True:
                try:
                    os.system('cls')
                    # Mostra o menu de opções
                    print(f'Endereço do servidor 1: {const.GRPC_SERVER_ADDRESS}:{const.GRPC_SERVER_PORT}\n')
                    print('\nMenu do Servidor 1')
                    print('===================\n')
                    print('1 - Registrar serviço')
                    print('2 - Consultar serviço')
                    print('3 - Desregistrar serviço')
                    print('4 - Obter todos os serviços')
                    print('5 - Voltar')
                    option = input('\nDigite uma opção: ')
                    if option == '1':
                        service_name = input('Digite o nome do serviço: ')
                        endpoint = input('Digite o endpoint do serviço: ')
                        # Registra o serviço
                        name_resolution_functions_server.register(service_name, endpoint)
                    elif option == '2':
                        service_name = input('Digite o nome do serviço: ')
                        # Consulta o serviço
                        name_resolution_functions_server.lookup(service_name)
                    elif option == '3':
                        service_name = input('Digite o nome do serviço: ')
                        # Desregistra o serviço
                        name_resolution_functions_server.unregister(service_name)
                    elif option == '4':
                        # Obtém todos os serviços
                        name_resolution_functions_server.all_services()
                    elif option == '5':
                        break
                    else:
                        print('Opção inválida')
                except grpc._channel._InactiveRpcError as e:
                    print(f'\nErro: O servidor 1 em questão não está ativo')
                    keyPressed = input('\n\nPressione ENTER qualquer tecla para continuar...')
        elif option == '2':
            while True:
                try:
                    os.system('cls')
                    print(f'Endereço do servidor 1: {const.GRPC_SERVER_ADDRESS}:{const.GRPC_SERVER_PORT}')
                    # Mostra o menu de opções
                    print('\nMenu do servidor 2')
                    print('===================\n')
                    print('1 - Registrar serviço')
                    print('2 - Consultar serviço')
                    print('3 - Desregistrar serviço')
                    print('4 - Obter todos os serviços')
                    print('5 - Voltar')
                    option = input('\nDigite uma opção: ')
                    if option == '1':
                        print('\n Registrando serviço')
                        service_name = input('Digite o nome do serviço: ')
                        endpoint = input('Digite o endpoint do serviço: ')
                        # Registra o serviço
                        name_resolution_functions_server2.register(service_name, endpoint)
                    elif option == '2':
                        print('\n Consultando serviço')
                        service_name = input('Digite o nome do serviço: ')
                        # Consulta o serviço
                        name_resolution_functions_server2.lookup(service_name)
                    elif option == '3':
                        print('\n Desregistrando serviço')
                        service_name = input('Digite o nome do serviço: ')
                        # Desregistra o serviço
                        name_resolution_functions_server2.unregister(service_name)
                    elif option == '4':
                        print('\n Obtendo todos os serviços')
                        # Obtém todos os serviços
                        name_resolution_functions_server2.all_services()
                    elif option == '5':
                        break
                    else:
                        print('Opção inválida')
                    print()
                except grpc._channel._InactiveRpcError as e:
                    print(f'\nErro: O servidor 2 em questão não está ativo')
                    keyPressed = input('\n\nPressione ENTER qualquer tecla para continuar...')
        elif option == '3':
            while True:
                try:
                    os.system('cls')
                    # Altera o endereço do servidor
                    print('\nAlterando endereço do servidor')
                    print('==============================\n')
                    print(f'Endereço atual servidor 1: {const.GRPC_SERVER_ADDRESS}:{const.GRPC_SERVER_PORT}')
                    print(f'Endereço atual servidor 2: {const.GRPC_SERVER_ADDRESS2}:{const.GRPC_SERVER_PORT}\n')
                    option = input('Digite o número do servidor que deseja alterar o endereço ou 3 para voltar: ')
                    if option == '1':
                        const.GRPC_SERVER_ADDRESS = input('Digite o endereço do servidor: ')
                        print('Endereço do servidor 1 alterado com sucesso')
                    elif option == '2':
                        const.GRPC_SERVER_ADDRESS2 = input('Digite o endereço do servidor: ')
                        print('Endereço do servidor 2 alterado com sucesso')
                    elif option == '3':
                        break
                    else:
                        print('Opção inválida')
                except grpc._channel._InactiveRpcError as e:
                    print(f'Erro: O servidor {option} em questão não está ativo')
                    keyPressed = input('\n\nPressione ENTER qualquer tecla para continuar...')
        elif option == '4':
            break
        else:
            print('Opção inválida')
    option = input('\n\nPressione ENTER qualquer tecla para continuar...')
    os.system('cls')

