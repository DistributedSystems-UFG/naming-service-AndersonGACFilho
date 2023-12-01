import grpc
import name_resolution_pb2
import name_resolution_pb2_grpc
import const
import socket
import name_resolution_functions

if __name__ == '__main__':
    # Exemplo de uso
    hostname=socket.gethostname()
    IPAddr=socket.gethostbyname(hostname)
    print("Your IP Address is: "+IPAddr)
    while True:
        print("1-Register\n2-Lookup\n3-Unregister\n4-All-Services\n5-Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            service_name=input("Enter service name: ")
            endpoint=input("Enter endpoint: ")
            name_resolution_functions.register(service_name, endpoint)
        elif choice==2:
            service_name=input("Enter service name: ")
            name_resolution_functions.lookup(service_name)
        elif choice==3:
            service_name=input("Enter service name: ")
            name_resolution_functions.unregister(service_name)
        elif choice==4:
            print("All services\n")
            name_resolution_functions.all_services()
            
        elif choice==5:
            break
        else:
            print("Invalid choice")
