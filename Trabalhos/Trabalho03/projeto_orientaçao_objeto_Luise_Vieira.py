#classe mae

class Veiculo:
    def __init__(self, marca, ano,cor):
        self.marca = marca #atributo publico
        self._cor = cor #atributo protegido
        self.__ano = ano #atributo privado
    @property #permite q um metodo de uma classe seja acessado como atributo normal.

    def ano(self):
        #retornar o ano do veiculo(getter)
        return self.__ano
        #setter atribui no __ano, privado
    @ano.setter 
    def ano(self,novo_ano):
        try: #validaçao com primeiro carro inventado
            if novo_ano >=1886:
                self.__ano = novo_ano
                print(f"Ano alterado para{novo_ano}")
            else:
                raise ValueError("Ano Invalido!")
        except ValueError as e:
                print(f"Erro ao alterar ano : {e}")
    def exibir_info(self):
         print(f"Marca: {self.marca}, Cor: {self._cor}, Ano: {self.__ano}")
class Carro(Veiculo):
    def __init__(self,marca,ano,cor,portas):
          super().__init__(marca,ano,cor)
          self.portas = portas

    def exibir_info(self):
     print(f"Carro: marca: {self.marca}, cor: {self._cor}, portas: {self.portas}, ano: {self.ano}")

class Moto(Veiculo):
    def __init__(self, marca, ano, cor, tipo):
        super().__init__(marca,ano,cor)
        
        self.tipo = tipo
    
    def exibir_info(self):
     print(f"Carro: marca: {self.marca}, cor: {self._cor}, tipo: {self.tipo}, ano: {self.ano}")

#instanciaçao
veiculo1= Veiculo("Generica", 2010, "branco")
carro1=  Carro("Toyota", 2010, "Prata", 4)
moto1=Moto("Honda",2019,"vermelho", "Esportiva")

#exibir inicial
veiculo1.exibir_info()
carro1.exibir_info()
moto1.exibir_info()

veiculo1.ano=2015
carro1.ano= 2025
moto1.ano= 1800

#exibir final
veiculo1.exibir_info()
carro1.exibir_info()
moto1.exibir_info()