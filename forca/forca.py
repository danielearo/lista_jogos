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

def desenhar_forca(erro):
    """Imprima o desenho da forca dependendo da quantidade de erros"""
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
    elif erro ==1:
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
   
    elif erro == 5:
        print (r"""
          _____
          |   |
          |  ( )
          |   |
          |  /|\
          |   |
          |  /
          """)
        
    elif erro == 6:
        print (r"""
          _____
          |   |
          |  ( )
          |   |
          |  /|\
          |   |
          |  / \
          """)
    