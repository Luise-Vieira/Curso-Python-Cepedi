from http.server import BaseHTTPRequestHandler, HTTPServer
#baseHTTP fornace os metodos para lidar com GET, POST...
#HTTP serve criam e manter ativo um servidor http, rodando em porta especifica 
import json #importa o formato de dados das respostas

alunos=[
    {"id":1, "nome": "Ana", "idade": 16 },
    {"id":2, "nome": "Carlos", "idade": 16 }
    ]

class MinhaAPI(BaseHTTPRequestHandler):
#a classe herda o BaseHTTP para usar os metodos HTTP
#MinhaAPI vai responder as requisiçoes
    def do_GET(self):
        if self.path=="/api/alunos":
            #if verifica se i caminho existe
            self.send_response(200)
            #envia o status http para o cliente
            self.send_header("Content-Type","application/json")
            #semd.header enviar um cabeçalho http
            #content-type vai informar o tipo de conteudo
            self.end_headers()#finaliza o cabeçalho para enviar a resposta
            resposta=json.dumps(alunos)#converte a lista de python para String
            self.wfile.write(resposta.encode("utf-8"))
            #envia os dados para o cliente , transforma a string em bytes para o servidor entender
        elif self.path.startswith("/api/alunos/"): #verifica se a url da api começa em /api/alunos
            try:
                alunos_id = int(self.path.split("/")[-1])
                #extrair o ID do aluno da URL e converter para inteiro
            except ValueError:
                self.send_response(400) #envia o erro "BAD REQUEST"
                self.end_headers()
                return #interrompe o metodo
            
            #procurar alunos
            aluno_encontrado= None
            for aluno in alunos:
                if aluno["id"] == alunos_id:
                    aluno_encontrado = aluno
                    break #sair do loop assim que o aluno for encontrado
            if aluno_encontrado:
                self.send_response(200)
                self.send_header("Content-Type","application/json")
                self.end_headers()

                resposta=json.dumps(aluno_encontrado)
                self.wfile.write(resposta.encode("utf-8"))
            else:
                self.send_response(404) #erro not found
                self.send_header("Content-Type","application/json")
                self.end_headers()

                erro= {"Erro:" "ALuno nao encontrado"}
                self.wfile.write(json.dumps(erro).encode("urf-8"))
        else:
            self.send_response(404)
            self.end_headers()
def main():

    servidor= HTTPServer(("localhost",8000),MinhaAPI)

    print("Servidor rodando em http://localhost:8000")
    servidor.serve_forever()
main()


