import socket_server

HOST, PORT = "localhost", 8657
server = socket_server.socketserver.TCPServer((HOST, PORT), socket_server.MyTCPHandler)

server.serve_forever()
