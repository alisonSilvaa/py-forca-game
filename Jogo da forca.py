palavra_chave = "koenigsegg"
palavra_lista = list(palavra_chave)
tamanho = len(palavra_lista)
forca = ['_'] * tamanho
acertou = True 
acertos = 0
tentativas = 0
chances = 10 
erros_forca = [] 
erros_resultado = ""


print("jogo da forca")
print("")
nome = input("digite seu nome: ")
print("")
print(f"Seja bem-vindo ao jogo {nome}")
print("") 
print("Dica do jogo: ")
print("É a marca de um dos carros mais velozes do mundo")

while chances > tentativas and tamanho > acertos:
    acertou = False
    letra_usuario = input("Digite a letra: ")
    for letra in range(tamanho):
        if letra_usuario == palavra_lista[letra] and forca[letra] == '_':
            forca[letra] = letra_usuario
            acertou = True 
            acertos+=1

    print("")
    palavra_m = ''.join(forca)
    print(palavra_m)
    print("")
    
    if acertou: 
        print(f"Parabéns {nome} você acertou a palavra")
    else: 
        erros_forca.append(letra_usuario)
        erros_resultado = ', '.join(erros_forca)
        tentativas+=1 
        print(f"Errou {nome}! Suas tentativas restantes são {chances - tentativas}")
        print(f"letras usadas: {erros_resultado}")
    
    print("")

    if acertos == tamanho:
        print(f"Meus parabéns {nome} você venceu o jogo! ")
    elif tentativas == chances:
        print(f"Lamento {nome} você perdeu o jogo ")
