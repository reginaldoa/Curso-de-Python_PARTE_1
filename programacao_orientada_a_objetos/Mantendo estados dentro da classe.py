# Mantendo estados dentro da classe

class Camera:
    def __init__(self, nome, filmando = False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f"{self.nome} ja esta filmando")
            return
        
        print(f"{self.nome} esta filmando")
        self.filmando = True


    def PararFilmar(self):
        if not self.filmando:
            print(f'{self.nome} desligada')
            return
        
        print(f"{self.nome} desligando....")
        self.filmando= False


    def fotogragar(self):
        if self.filmando:
            print(f"{self.nome} nao pode fotografar filmando")
            return
        

        print(f"{self.nome} esta fotografando")


c1 = Camera("Canon")
c2 = Camera("Sony")


c1.filmar()
c1.filmar()
c1.PararFilmar()
c1.PararFilmar()
c1.filmar()
c1.fotogragar()
c1.PararFilmar()
c1.fotogragar()


#print(c1.filmando)
#print(c2.filmando)
