from http.server import BaseHTTPRequestHandler, HTTPServer
import json 
import hashlib #gerar token 

host = "localhost"
PORT = 8000
TOKENS = {}

def gerar_token (usuario):
    return hashlib.sha256(usuario.encode()).hexdigest()

class APISimples (BaseHTTPRequestHandler):
    def do_POST (self):
        #verificar se a requisicao é para o endpoint / login
        if  self.path == "/login":
            tamanho = int(self.headers["Content-Length"])
            #le os dados da requisiçao
            corpo = self.rfile.read(tamanho)
            dados = self.rfile.loads(corpo)

            usuario = dados.get("user")
            senha = dados.get("password")

            with open ("users.json") as f :
                users = json.load(f)

            if usuario in users and users[usuario]["password"] == senha :
                token = gerar_token(usuario)
                TOKENS[token] = users[usuario]["role"]

                self.send_response(200)
                self.send_header("Content-Type","application/json")
                self.end_headers()

                self.wfile.write(json.dumps({
                    "token" : token
                    
                }).encode())
            else:
                self.send_response(401)
                self.end_headers()
    def do_GET (self):
        if self.path == "/soma" :
            auth = self.headers.get("Authorization")
            if auth not in TOKENS:
                self.send_response(403)
                self.end_headers()
                return
            resultado = 10 + 20                
            self.send_response(200)
            self.send_header("Content-Type","application/json")
            self.end_headers()

            self.wfile.write(json.dumps({
                    "resultado" : resultado
                }).encode())
            
server = HTTPServer((host, PORT), APISimples)
print("API REST rodando em http :// localhost:8000")
server.serve_forever()

#criaçao do nosso websocket

import socket
import threading

def websocket_server():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(("localhost", 9000))
    servidor.listen(1)

    print("Websocket rodando em : ws://localhost:9000")

    while True :
        cliente, endereco = servidor.accept()
        mensagem = cliente.recv(1024).decode()

        if not mensagem:
            break

        print("Mensagem recebida ",mensagem)
        resposta = f"Servirdor recebeu: {mensagem}"
        cliente.send(resposta.encode())
        cliente.close()

        threading.Thread(target = websocket_server).start()