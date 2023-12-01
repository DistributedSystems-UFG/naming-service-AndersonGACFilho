import grpc
import name_resolution_pb2
import name_resolution_pb2_grpc
import const
import socket
import name_resolution_functions

if __name__ == '__main__':
    # Exemplo de uso
    while True:
        print("1-Lookup\n2-All-Services\n3-Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            service_name=input("Enter service name: ")
            name_resolution_functions.lookup(service_name)
        elif choice==2:
            print("All services\n")
            name_resolution_functions.all_services()
        elif choice==3:
            break
        else:
            print("Invalid choice")

