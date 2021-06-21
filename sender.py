import socket                               #importing socket module / library to creat
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
recv_addr=("127.0.0.1",5809)
user_data=input("Enter your message :- ")
new_data=user_data.encode('ascii')
s.sendto(new_data,recv_addr)
print("Message has been send....")