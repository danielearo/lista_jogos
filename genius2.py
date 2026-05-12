import os
import time
import random

dicionario_cores = {"VERDE": "20",
                    "AZUL": "90",
                    "AMARELO": "60",
                    "VERMELHO": "C0",
                    "LILAS": "D0"}

lista_sequencia=[]

def limpar_tela():
    os.system("color 07")
    os.system("cls")

def mudar_cor(cor): # para criar um parâmetro é só colocar dentro do ()
    codigo_cor = dicionario_cores[cor]
    os.system(f"color {codigo_cor}")
    time.sleep(1)
    limpar_tela()

print("""

    ***************************************************
    ***                                             ***
    ***                 GENIUS                      ***
    ***        ----------------------------         ***
    ***                                             ***
    ***         Repita as cores sem errar           ***
    ***                                             ***
    ***************************************************
      
      """)

input("Pressione ENTER para começar...")

limpar_tela()

lista_cores = ["VERDE", "AZUL", "AMARELO","VERMELHO","LILAS"]


while True:
    cor_aleatoria = random.choice(lista_cores) #essa função criar uma lista aleatória

    lista_sequencia.append(cor_aleatoria) #insiro a cor aleatoria dentro da lista_sequencia que irá guardar todas cores

    #percorro a lista e utilizo a função mudar_cor para exibir as cores
    for cor_lista in lista_sequencia:
        mudar_cor(cor_lista)

#perguntado a sequencia de cores, um menu
    print("""
        V = VERDE
        A = AZUL
        M = AMARELO
        R = VERMELHO
        L = LILAS
          """)

    resposta= input("Digite a sequência correta:  ").upper()

    dicionario_abreviacoes= {"V" : "VERDE",
                             "A" : "AZUL", 
                             "M" : "AMARELO",
                             "R" : "VERMELHO",
                             "L" : "LILAS"}
    #transformando uma resposta em uma lista 
    lista_resposta= []

    for letra in resposta:
        cor = dicionario_abreviacoes.get(letra)
        lista_resposta.append(cor)
    
    if lista_resposta != lista_sequencia:
        print("Você errou, gosso")
        print("A sequência era: ")
        print(*lista_sequencia)
        break
    else:
        print("Você acertou, miserpavi")
        print("Vamos para a proxima fase")
        input("Aperte ENTER quando estiver pronto...")
        limpar_tela()
    








