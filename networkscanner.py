import socket
def scan_ports(target_ip,start_port,end_port):
    open_ports=[]
    for port in range(start_port,end_port+1):
        try:
            sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(0.00001)
            result=sock.connect_ex((target_ip,port))
            if result==0:
                open_ports.append(port)
            sock.close()
        
        except socket.error:
            pass
    
    return open_ports

target_ip=input("Target ip: ")


start_port=int(input("Start port: "))
end_port=int(input("End port: "))

open_ports=scan_ports(target_ip,start_port,end_port)

if open_ports:
    print("Open ports: ")
    for i in open_ports:
        print("Port number:",i)
else:
    print("Open ports not found")