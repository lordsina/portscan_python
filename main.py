import socket

for x in range(20,443):
     a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     #   AF_INET = IP V4 ---- AF_INET6 (IPv6 protocol)
     # SOCK_STREAM: TCP(reliable, connection oriented)
     # SOCK_DGRAM: UDP(unreliable, connectionless)



     location = ("135.125.161.63",x)
     result_of_check = a_socket.connect_ex(location)
     if result_of_check == 0:
      print(x)
     a_socket.close()


