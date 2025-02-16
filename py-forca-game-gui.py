import sys
import random
from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, QSize


class forca():
    def __init__(self, janela):

        #instanciar

        self.janela = janela 

        # variaveis

        self.acertou = False
        self.acertos = 0
        self.tentativas = 0
        self.chances = 6
        self.palavra = self.list_de_palavras().lower()
        self.palavra_chave = list(self.palavra)
        self.tamanho_vetor = len(self.palavra_chave)
        self.forca_erros = []
        self.ajuda_max=0
        self.list_ajudas = []

        #self.forca modificado com espaço

        self.forca = list(self.palavra)
        for i in range(self.tamanho_vetor):
            if self.forca[i].isalpha():
                self.forca[i] = '_'
        
        #self.list_ajuda modificado pra ficar sem espaço e numeros

        for i in range(self.tamanho_vetor):
            if self.palavra_chave[i].isalpha():
                self.list_ajudas.append(self.palavra_chave[i])
        
        self.tamanho_caract = sum(1 for i in self.forca if '_' == i)
        self.espaco = self.tamanho_vetor - self.tamanho_caract

    def list_de_palavras(self):
        
        self.carros = [
    # JDM Classics
    "Toyota Supra", "Nissan Skyline", "Mazda RX-7", "Honda NSX", "Subaru WRX",
    "Mitsubishi Lancer", "Nissan Silvia", "Toyota AE86", "Mazda RX-8", "Honda Civic",
    "Toyota Celica", "Nissan 300ZX", "Mitsubishi 3000GT", "Honda S2000", "Nissan Fairlady",
    "Lexus LFA", "Nissan GT-R", "Toyota GR Supra", "Mazda MX-5", "Acura Integra",
    "Toyota MR2", "Subaru BRZ", "Toyota GR86", "Nissan Pulsar", "Toyota Chaser",
    "Infiniti G35", "Honda Prelude", "Mitsubishi Eclipse", "Mazda Cosmo", "Nissan Stagea",

    # Supercarros
    "Lamborghini Aventador", "Ferrari 488", "McLaren 720S", "Bugatti Chiron", "Porsche 911",
    "Lamborghini Huracán", "Ferrari F8", "McLaren P1", "Pagani Huayra", "Koenigsegg Agera",
    "Bugatti Veyron", "McLaren Senna", "Ferrari LaFerrari", "Aston Martin DBS", "Lamborghini Murciélago",
    "Porsche Carrera", "Pagani Zonda", "Ferrari Enzo", "McLaren F1", "Aston Martin Valkyrie",

    # Muscle Cars V8
    "Ford Mustang", "Chevrolet Camaro", "Dodge Challenger", "Chevrolet Corvette", "Ford Mustang Mach 1",
    "Dodge Charger", "Chevrolet Chevelle", "Pontiac GTO", "Plymouth HEMI Cuda", "Ford Mustang Boss",
    "Dodge Viper", "Chevrolet Impala", "Ford Falcon", "Dodge Demon", "Chevrolet Nova",
    "Ford Torino", "Buick GSX", "Oldsmobile 442",

    # Carros Populares
    "Volkswagen Golf", "Ford Focus", "Renault Megane", "Fiat Uno", "Volkswagen Gol",
    "Chevrolet Opala", "Fiat Palio", "Ford Escort", "Volkswagen Fusca", "Chevrolet Corsa",
    "Honda Fit", "Toyota Corolla", "Honda Civic", "Volkswagen Jetta", "Chevrolet Onix",
    "Hyundai HB20", "Renault Sandero", "Peugeot 208", "Toyota Hilux", "Chevrolet S10", "Ford Ranger"
]


        return ''.join(random.sample(self.carros, 1))

    def central(self):
        if self.chances > self.tentativas and self.tamanho_caract > self.acertos:
            palavra_usuario = self.janela.input.text()
            self.acertou = False
            self.janela.input.clear()
            
            if len(palavra_usuario) != 1:
              self.janela.resultado.setText(f"digite apenas UM CARACTERE!")  
              return

            if palavra_usuario.isalpha(): 
                palavra_usuario = palavra_usuario.lower()
                if palavra_usuario in self.forca or palavra_usuario in self.forca_erros:
                    self.janela.resultado.setText(f"a palavra '{palavra_usuario}' ja foi escolhida!")
                else:
                    for letra in range(self.tamanho_caract + self.espaco):
                        if palavra_usuario == self.palavra_chave[letra] and self.forca[letra] == '_':
                            self.forca[letra] = palavra_usuario
                            self.acertos+=1
                            self.list_ajudas = [letra for letra in self.list_ajudas if palavra_usuario != letra]
                            self.acertou=True

                    self.palavra_mostra = ''.join(self.forca)
                    self.janela.forca.setText(self.palavra_mostra)

                    if self.acertou:
                        self.janela.resultado.setText("Parabéns você acertou!")
                    else:
                        self.tentativas+=1 
                        self.janela.resultado.setText(f"Você errou! suas tentativas restantes são: {self.chances - self.tentativas}")
                        self.forca_erros.append(palavra_usuario)
                        self.list_erro_string = ','.join(self.forca_erros)
                        self.janela.forca_erro.setText(self.list_erro_string)
                        self.fisica_forca()  
            else: 
                self.janela.resultado.setText("Digite um caracter do alfabeto")

        if self.acertos == self.tamanho_caract:
            self.janela.resultado.setText("Parabéns você venceu o jogo!")
            self.janela.botao.show()
            self.janela.botao_ajuda.hide()
        elif self.tentativas == self.chances:
            self.janela.forca.setText(f"A palavra certa era: {self.palavra}")
            self.janela.resultado.setText("Parabéns você perdeu o jogo! ")
            self.janela.botao.show()
            self.janela.botao_ajuda.hide()

    def reinicio(self):
        self.janela.cabeca1.hide()
        self.janela.corpo2.hide()
        self.janela.braco_esquerdo3.hide()
        self.janela.braco_direito4.hide()
        self.janela.perna_esquerda5.hide()
        self.janela.pernadireita6.hide()
        
        self.janela.botao.hide()
        self.janela.botao_ajuda.show() 

        self.acertos = 0
        self.tentativas = 0 
        self.forca_erros = []
        self.ajuda_max = 0

        self.palavra = self.list_de_palavras().lower()
        self.palavra_chave = list(self.palavra)
        self.tamanho_vetor = len(self.palavra_chave)
        self.list_ajudas.clear()

        self.forca = list(self.palavra)
        for i in range(self.tamanho_vetor):
            if self.forca[i].isalpha():
                self.forca[i] = '_'

        for i in range(self.tamanho_vetor):
            if self.palavra_chave[i].isalpha():
                self.list_ajudas.append(self.palavra_chave[i])

        self.tamanho_caract = sum(1 for i in self.forca if '_' == i)
        self.espaco = self.tamanho_vetor - self.tamanho_caract

        self.palavra_mostra = ''.join(self.forca)
        self.list_erro_string = ""
        self.janela.resultado.setText("Jogo Reiniciado")
        self.janela.forca.setText(self.palavra_mostra)
        self.janela.forca_erro.setText(self.list_erro_string) 
        
    
    def ajuda(self):
        if self.ajuda_max < 3:
            self.palavra_ajuda = ''.join(random.choice(self.list_ajudas))
            self.list_ajudas = [letra for letra in self.list_ajudas if letra != self.palavra_ajuda]
            for i in range(self.tamanho_vetor):
                if self.palavra_ajuda == self.palavra_chave[i] and self.forca[i] == '_':
                    self.forca[i] = self.palavra_ajuda
                    self.acertos+=1
            self.ajuda_max+=1
            self.palavra_mostra1 = ''.join(self.forca)
            self.janela.forca.setText(self.palavra_mostra1)
            if self.ajuda_max == 3: 
                self.janela.botao_ajuda.hide() 
            elif self.acertos == self.tamanho_caract:
                self.central()

    def fisica_forca(self):
        if self.tentativas == 1: 
            self.janela.cabeca1.show()
        elif self.tentativas == 2:
            self.janela.corpo2.show()
        elif self.tentativas == 3:
            self.janela.braco_esquerdo3.show()
        elif self.tentativas == 4:
            self.janela.braco_direito4.show()
        elif self.tentativas == 5:
            self.janela.perna_esquerda5.show()
        elif self.tentativas == 6:
            self.janela.pernadireita6.show()


    def teste(self):
        print(f"palavra: {self.palavra}")
        print(f"lista de ajuda: {''.join(self.list_ajudas)}")
        print(f"forca : {''.join(self.forca)} \n")
        
        print(f"acertos: {self.acertos}")
        print(f"tamanho caract: {self.tamanho_caract} \n")
        
class minhaJanela (QWidget):
    def __init__(self):
        super().__init__()

        #criação da janela

        self.setWindowTitle("Forca game")
        self.resize(1280,720)

        #instancias

        self.forca_game = forca(self)
        self.layouts = QVBoxLayout()
        self.layouts_h = QHBoxLayout()

        # conectando o objeto de funções com a tela

        self.setLayout(self.layouts)
        self.setLayout(self.layouts_h)
        
        #outros

        espaço_inicial = ''.join(self.forca_game.forca)

        #criando, personalizando e alinhando o rotulo,campos de entrada e botões.

            #forca_principaçal e suas etapas... 

        self.forca_principal = QLabel(self) 
        self.img_forca0 = QPixmap(r"C:\Users\yotub\Desktop\GitHub\Python\py-forca-game-gui\img\forca_principal.png")
        self.forca_principal.setPixmap(self.img_forca0)
        self.forca_principal.setGeometry(0,0,1280,720)

        self.cabeca1 = QLabel(self)
        self.img_cabeca1 = QPixmap(r"C:\Users\yotub\Desktop\GitHub\Python\py-forca-game-gui\img\cabeça1.png")
        self.cabeca1.setPixmap(self.img_cabeca1)
        self.cabeca1.setGeometry(0,0,1280,720)
        self.cabeca1.hide()

        self.corpo2 = QLabel(self) 
        self.img_corpo2 = QPixmap(r"C:\Users\yotub\Desktop\GitHub\Python\py-forca-game-gui\img\corpo2.png")
        self.corpo2.setPixmap(self.img_corpo2)
        self.corpo2.setGeometry(0,0,1280,720)
        self.corpo2.hide()

        self.braco_esquerdo3 = QLabel(self)
        self.img_braco_esquerdo = QPixmap(r"C:\Users\yotub\Desktop\GitHub\Python\py-forca-game-gui\img\braço esquerdo3.png")
        self.braco_esquerdo3.setPixmap(self.img_braco_esquerdo)
        self.braco_esquerdo3.setGeometry(0,0,1280,720)
        self.braco_esquerdo3.hide()

        self.braco_direito4 = QLabel(self)
        self.img_braco_direito4 = QPixmap(r"C:\Users\yotub\Desktop\GitHub\Python\py-forca-game-gui\img\braçodireito4.png")
        self.braco_direito4.setPixmap(self.img_braco_direito4)
        self.braco_direito4.setGeometry(0,0,1280,720)
        self.braco_direito4.hide()

        self.perna_esquerda5 = QLabel(self)
        self.img_perna_esquerda5 = QPixmap(r"C:\Users\yotub\Desktop\GitHub\Python\py-forca-game-gui\img\perna esquerda5.png")
        self.perna_esquerda5.setPixmap(self.img_perna_esquerda5)
        self.perna_esquerda5.setGeometry(0,0,1280,720)
        self.perna_esquerda5.hide()

        self.pernadireita6 = QLabel(self)
        self.img_pernadireita6 = QPixmap(r"C:\Users\yotub\Desktop\GitHub\Python\py-forca-game-gui\img\pernadireita6.png")
        self.pernadireita6.setPixmap(self.img_pernadireita6)
        self.pernadireita6.setGeometry(0,0,1280,720)
        self.pernadireita6.hide()

        self.forca = QLabel(espaço_inicial,self)
        self.forca.setFont(QFont("Arial",30))
        self.forca.setAlignment(Qt.AlignCenter)

        self.resultado = QLabel("Exibir a resultado",self)
        self.resultado.setFont(QFont("Arial",30))
        self.resultado.setAlignment(Qt.AlignCenter)

        self.input = QLineEdit(self)
        self.input.setFont(QFont("Arial",40))
        self.input.setAlignment(Qt.AlignCenter)

        self.forca_erro = QLabel("",self)
        self.forca_erro.setFont(QFont("Arial",20))
        self.forca_erro.setGeometry(80,-5,200,40)

        self.rotulo_erro = QLabel("Erros: ",self)
        self.rotulo_erro.setFont(QFont("Arial",20))

        self.botao = QPushButton("Reiniciar",self)
        self.botao.setFont(QFont("Arial",20))
        self.botao.setFixedSize(QSize(200,40))
        self.botao.setGeometry(535,539,0,0)
        self.botao.hide()

        self.botao_ajuda = QPushButton("Ajuda")
        self.botao_ajuda.setFont(QFont("Arial",20))
        self.botao_ajuda.setFixedSize(QSize(200,40))

        self.botao_teste = QPushButton("Teste")
        self.botao_teste.setFont(QFont("Arial",20))
        self.botao_teste.setFixedSize(QSize(200,40))
        self.botao.setGeometry(535,300,0,0)
    
        #ordenando os rotulos        

        self.layouts.addWidget(self.forca)
        self.layouts.addWidget(self.resultado)
        self.layouts.addWidget(self.botao_ajuda)
        self.layouts.addWidget(self.input)
        self.layouts.addWidget(self.botao_teste)
        
        
        # ativação da class forca 
    
        self.input.returnPressed.connect(self.forca_game.central)
        self.botao.clicked.connect(self.forca_game.reinicio)
        self.botao_ajuda.clicked.connect(self.forca_game.ajuda)
        self.botao_teste.clicked.connect(self.forca_game.teste)
        

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    janela = minhaJanela()
    janela.show()
    sys.exit(app.exec_())
