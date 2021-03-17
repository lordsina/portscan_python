import socket
from rich.console import Console
from rich.table import Table
console = Console()
table = Table(show_header=True, header_style="bold red")
table.add_column("port", style="dim", width=12)
table.add_column("Title")
table.add_column("status", justify="center")




for x in range(18,26):
     a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     #   AF_INET = IP V4 ---- AF_INET6 (IPv6 protocol)
     # SOCK_STREAM: TCP(reliable, connection oriented)
     # SOCK_DGRAM: UDP(unreliable, connectionless)
     location = ("135.125.161.63",x)
     result_of_check = a_socket.connect_ex(location)
     if result_of_check == 0:
          table.add_row(
               "[red]"+str(x)+"[/red]",
               "[red]HELLO[/red]",
               "OPEN",
          )
     a_socket.close()


console.print(table)