from http.server import BaseHTTPRequestHandler, HTTPServer
#baseHTTP fornace os metodos para lidar com GET, POST...
#HTTP serve criam e manter ativo um servidor http, rodando em porta especifica 
import json #importa o formato de dados das respostas

alunos=[
    {"id":1, "nome": "Ana", "idade": 16 },
    {"id":2, "nome": "Carlos", "idade": 17 },
    {"id":3, "nome": "João", "idade": 18 },
    {"id":4, "nome": "Maria", "idade": 19 },
    {"id":5, "nome": "Caua", "idade": 20 }

    ]

def proximo_id(): #garamte que cada aluno tenha um ID unico
    return max(aluno["id"] for aluno in alunos)+1 if alunos else 1 

    #busca o ID maximo e adiciona mais um, se nao houver alunos retorna 1
class MinhaAPI (BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/api/alunos":
            #if verifica se i caminho existe
            self.send_response(200)
            #envia o status http para o cliente
            self.send_header("Content-Type","application/json")
            #send.header enviar um cabeçalho http
            #content-type vai informar o tipo de conteudo
            self.end_headers()#finaliza o cabeçalho para enviar a resposta
            resposta=json.dumps(alunos)#converte a lista de python para String
            self.wfile.write(resposta.encode("utf-8"))

        elif self.path.startswith("/api/alunos"):
            
            try:
                aluno_id = int(self.path.split("/")[-1])
                #extrair o ID do aluno da URL e converter para inteiro
            except ValueError:
                self.send_response(400) #envia o erro "BAD REQUEST"
                self.end_headers()
                return #interrompe o metodo
            
            for aluno in alunos:
                if aluno["id"] == aluno_id:
                    self.send_response(200)
                    self.send_header("Content-Type","application/json")
                    self.end_headers
                    self.wfile.write(json.dumps(aluno).encode("utf-8"))
          
            self.send_response(404)
            self.send_header("Content-Type","application/json")
            self.end_headers
            self.wfile.write(json.dumps({"erro":"Aluno nao encontrado"}).encode("uft-8"))
        else:
            self.send_response(404)
            self.end_headers()
        
        #criação de metodos
    def do_POST(self):
            if self.path=="api/alunos/":
                tamanho=int(self.headers.get("Content-Lenght",0))

                corpo= self.rfile.read(tamanho)
                dados = json.loads(corpo)

                if "nome" not in dados or "idade" not in dados:
                    self.send_response(404)
                    self.headers()
                    return
                    
                novo_aluno = {
                    "id": proximo_id(),
                    "nome": dados["nome"],
                    "idade": dados["idade"]
                    }
                alunos.append(novo_aluno)

                self.send_response(201)
                self.send_header("Content-Type")
                self.end_headers()
                self.wfile.write(json.dumps(novo_aluno).encode("utf-8"))

    def do_PUT(self): #atualizar TUDO

        if self.path == "/api/alunos":
            try:
                 aluno_id = int(self.path.split("/")[-1]) 
            except ValueError:
                self.send_response(400) # envia o erro "BAD REQUEST"
                self.end_headers()
                return 
            
            tamanho=int(self.headers.get("Content-Lenght",0))
            corpo= self.rfile.read(tamanho)
            dados = json.loads(corpo)

            for aluno in alunos:
                if aluno ["id"] == aluno_id:
                    #atualizar os dados
                    aluno["nome"] = dados.get("nome", aluno["nome"])
                    aluno["nome"] = dados.get("idade", aluno["idade"])
                    self.send_response(200)
                    self.send_header("Content-Type","application/json")
                    self.end_headers
                    self.wfile.write(json.dumps(aluno).encode("utf-8"))
                    return
            self.send_response(404)
            self.end_headers()

    def do_PATCH(self): #atualização parcial

        if self.path == "/api/alunos":
            try:
                 aluno_id = int(self.path.split("/")[-1]) 
            except ValueError:
                self.send_response(400) # envia o erro "BAD REQUEST"
                self.end_headers()
                return 
            
            tamanho=int(self.headers.get("Content-Lenght",0))
            corpo= self.rfile.read(tamanho)
            dados = json.loads(corpo)

            for aluno in alunos:
                #atualizar os campos enviados individualmente
                if aluno["id"]== aluno_id:
                    if "nome" in dados:
                        aluno["nome"] = dados["nome"]
                    if "idade" in dados:
                        aluno["idade"] = dados ["idade"]
                    self.send_response(200)
                    self.send_header("Content-Type","application/json")
                    self.end_headers
                    self.wfile.write(json.dumps(aluno).encode("utf-8"))
                    return
            self.send_response(404)
            self.end_headers()
        
    def do_DELETE(self):
            
        if self.path == "api/alunos":
            try:
                 aluno_id = int(self.path.split("/")[-1]) 
            except ValueError:
                self.send_response(400) # envia o erro "BAD REQUEST"
                self.end_headers()
                return 
            
            for aluno in alunos:
                if aluno["id"]==aluno_id:
                    alunos.remove(aluno)
                    self.send_response(204)
                    self.end_headers()
                    return
            self.send_response(404)
            self.end_headers()

def main():
    servidor = HTTPServer(("localhost",8000),MinhaAPI)
    print("API rodando em http://localhost:8000")
    servidor.serve_forever()
main()