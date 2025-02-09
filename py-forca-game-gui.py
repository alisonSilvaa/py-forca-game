import sys
from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class forca():
    def __init__(self, janela):

        #instanciar

        self.janela = janela 

        # variaveis

        self.acertou = False
        self.acertos = 0
        self.tentativas = 0
        self.chances = 10
        self.palavra = "toyota supra drift" 
        self.palavra_chave = list(self.palavra)
        self.tamanho_vetor = len(self.palavra_chave)
        self.forca_erros = []

        #self.forca modificado com espaço

        self.forca = list(self.palavra)
        for i in range(self.tamanho_vetor):
            if self.forca[i].isalpha():
                self.forca[i] = '_'
        
        self.tamanho_caract = sum(1 for i in self.forca if '_' == i)
        self.espaco = self.tamanho_vetor - self.tamanho_caract

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
            else: 
                self.janela.resultado.setText("Digite um caracter do alfabeto")

        if self.acertos == self.tamanho_caract:
            self.janela.resultado.setText("Parabéns você venceu o jogo!")
            self.janela.botao.show()
        elif self.tentativas == self.chances:
            self.janela.resultado.setText("Parabéns você perdeu o jogo! ")
            self.janela.botao.show()

    def reinicio(self):
        self.janela.botao.hide()
        self.acertos = 0
        self.tentativas = 0 
        self.forca_erros = []

        self.forca = list(self.palavra)
        for i in range(self.tamanho_vetor):
            if self.forca[i].isalpha():
                self.forca[i] = '_'

        self.palavra_mostra = ''.join(self.forca)
        self.list_erro_string = ""
        self.janela.resultado.setText("Jogo Reiniciado")
        self.janela.forca.setText(self.palavra_mostra)
        self.janela.forca_erro.setText(self.list_erro_string) 
        
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

        self.forca = QLabel(espaço_inicial,self)
        self.forca.setFont(QFont("Arial",40))
        self.forca.setAlignment(Qt.AlignCenter)

        self.resultado = QLabel("Exibir a resultado",self)
        self.resultado.setFont(QFont("Arial",40))
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
        self.botao.hide()
        

        #ordenando os rotulos        

        self.layouts.addWidget(self.forca)
        self.layouts.addWidget(self.resultado)
        self.layouts.addWidget(self.botao)
        self.layouts.addWidget(self.input)
        
        # ativação da class forca 
    
        self.input.returnPressed.connect(self.forca_game.central)
        self.botao.clicked.connect(self.forca_game.reinicio)
        

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    janela = minhaJanela()
    janela.show()
    sys.exit(app.exec_())
