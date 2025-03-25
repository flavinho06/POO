class Cachorro:
    def __init_   (self,nome,idade,raca,comida,):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.comida = comida
        self.energia = 100
        self.acordado = False
        self.feliz = False
    
    def comer(self):
        if self.acordado is True:
         self.comida -=1
         print(f"{self.nome} terminou de comer")
        else:
           print(f"{self.nome} está dormindo e não pode comer") 
    
    def dormir(self):
        self.acordado = False
        self.energia = 100
        print(f"{self.nome} está revigorado")
        print(f"{self.nome} está dormindo") 
    
    def acordar(self):
        self.acordado = True
        print(f"{self.nome} está acordado")
    
    def latir(self):
       if self.acordado = False
        print(f"{self.nome} está dormindo")
       else:
        print(f"{self.nome} Latiu: AU AU!")
    
    def brincar(self):
       
       if self.acordado:
            if self.energia >= 20:
              self.energia -=20
              self.feliz = True
              print(f"{self.nome} está brincando feliz")
            else:
               print(f"{self.nome} está exausto")
          
       else:
          print(f"{self.nome} está dormindo e não pode brincar")
    
    def ignorar(self):
       if self.acordado is True:
          self.feliz = False
          print(f"{self.nome} foi ignorado e está triste")
       else:
           print(f"{self.nome} está dormindo")
    


             

cachorro1= Cachorro("Cookie",8,"Poddle",3)
cachorro2= Cachorro("Mary",100,"Pastor Australiano",3)

cachorro1.acordar()
cachorro1.comer()

cachorro2.acordar()
cachorro2.comer()
