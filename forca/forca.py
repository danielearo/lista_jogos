import os
import random

def limpar(): 
    """função limpar a tela do prompt"""
    os.system("cls")

def escolher_palavra() -> str: #str significa que só pode texto
    """Escolhe e retorna uma palavra aleatória"""
    palavras = ["GODOFREDO", 
                "AMENDOIM", 
                "BICICLETA", 
                "ELEFANTE", 
                "GIRASSOL", 
                "MONTANHA", 
                "TORNEIRA"
                ]
    palavra_aleatoria = random.choice(palavras)
    return palavra_aleatoria #retorna a palavra para quem chamou a função

#palavra_escolhida = escolher_palavra()

#print(palavra_escolhida)

def desenhar_forca(erro:int):
    """Imprima o desenho da forca dependendo da quantidade de erros"""
    limpar()

    if erro == 0:
        print(r"""
          _____
          |   |
          |
          |
          |
          |
          |
          """)
    elif erro == 1:
        print (r"""
          _____
          |   |
          |  ( )
          |
          |
          |
          |
          """)
    
    elif erro == 2:
        print (r"""
          _____
          |   |
          |  ( )
          |   |
          |   |
          |
          |
          """)
    elif erro == 3:
        print (r"""
          _____
          |   |
          |  ( )
          |   |
          |  /|
          |
          |
          """)
   
    elif erro == 4:
        print (r"""
          _____
          |   |
          |  ( )
          |   |
          |  /|\
          |   |
          |  /
          """)
        
    elif erro == 5:
        print (r"""
          _____
          |   |
          |  ( )
          |   |
          |  /|\
          |   |
          |  / \
          """)
    
#desenhar_forca(5) - somente para testar se está correto

def gerar_tracos(palavra: str) -> list:
    """Gera e retorna uma lista contendo underlines (_) na mesma quantidade que as letras da palavra"""
    quantidade_de_letras = len(palavra)  #len significa a quantidade letras;
    tracos = []

    #usando while e contador
    contador = 0
    while contador < quantidade_de_letras:
        tracos.append("_")
        contador = contador + 1

    #outra forma, comparando a quantidade de itens de _ na lista traços;
    #while len(tracos) < quantidade_de_letras:
        #tracos.append("_")

    #outra forma, usando for
    #for X in palavra:
        #tracos.append("_")

    return tracos

# lista_tracos = gerar_tracos("CASA")
# print(*lista_tracos)

def perguntar_letra() -> str:
    #pergunta uma letra
    resposta = input("Escolha uma letra:").upper() #letra maiuscula
    
    while len(resposta) !=1:
        resposta = input("Eu disse apenas UMA letra: ").upper()
        return resposta
    
letra = perguntar_letra()
print(letra)

