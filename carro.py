class Carro:
    def _init(self,modelo,ano,cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.combustivel = 0
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if self.combustivel > 0:
            self.ligado = True
            print(f"O carro de modelo {self.modelo} ligou!")
        else: print(f"O carro de modelo {self.modelo} está sem combustível.")

    def desligar(self):
        if self.velocidade == 0:
            self.ligado = False
            print(f"O carro {self.modelo} foi desligado!!")
        else:
            print(f"Esse {self.modelo} está em movimento, não pode desligar.")
    
    def acelerar(self):
        if self.ligado is True:
            if self.comnbustivel >= 5:        
                self.velocidade += 10
                self.combustivel -= 5
                print(f"Seu {self.modelo} está a {self.velocidade} km/h.")
            else: print(f"O {self.modelo} está desligado e não popde acelerar.")

    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 10
            print(f"O {self.modelo} freou, está {self.velocidade} km/h")
        else: 
            print(f"Esse{self.modelo} já está parado")

    def abastecer(self, quantidade):
        if self.combustivel + quantidade < 100:
            self.combustivel += quantidade
            print(f"Seu carro {self.modelo}foi abastecido, o combustível está agora em: {self.combustivel}")
        else:
            print(f"O tanque está acima do limite de combustível")
        

    def buzinar(self):
        print(f"{self.modelo}: BEEP BEEP!!")


    def status(self):
         print(f"Modelo: {self.modelo}")
       print(f"Ano: {self.ano}:")
       print(f"cor: {self.cor}")
       print(f"combustível: {self.combustivel}")
       print(f"velocidade atual: {self.velocidade} km/h")
       print(f"ligado: {self.ligado}")
       print(f"Limite de velocidade: {self.limite_velocidade} km/h")





carro1= Carro("Fusca",1897,"Azul")
carro2= Carro("HB20",2000,"Loira Odonto")

carro1.ligar()
carro1.buzinar()
carro1.abastecer(50)
carro1.status()
carro1.ligar()
carro1.acelerar()
carro1.frear()

carro2.abastecer(80)
carro2.ligar()
carro2.buzinar()
carro2.status()
carro1.desligar()
carro1.acelerar()
carro1.ligar()
for i in range(4):
 carro1.acelerar()

carro1.desligar()
for i in range(10):
 carro1.frear()
