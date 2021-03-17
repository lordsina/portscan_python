import socket

for x in range(20,443):
     a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     location = ("135.125.161.63",x)
     result_of_check = a_socket.connect_ex(location)
     if result_of_check == 0:
      print(x)
     a_socket.close()


