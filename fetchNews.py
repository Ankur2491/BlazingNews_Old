import json
import SimpleHTTPServer
import SocketServer
PORT = 9876
fileName = "news.txt"
with open(fileName,"r") as read_file:
    data = json.load(read_file)
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("",PORT),Handler)
httpd.server_version
