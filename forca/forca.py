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
          |   |
          |
          """)
    elif erro == 3:
        print (r"""
          _____
          |   |
          |  ( )
          |   |
          |  /|
          |   |
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
    
def jogar_forca():
    #tela inicial do jogo
    print("""
          ______________________________
          XX                          XX
          XX         FORCA            XX
          XX ________________________ XX
          XX                          XX
          XX     Acerte ou morra!     XX
          XX ________________________ XX
             """)
    
    input("Aperte ENTER para apostar a sua vida...")

    contador_erro = 0 

    #chamar a função escolher_palavra e guardar em uma variavel
    palavra_escolhida = escolher_palavra()

    #chamar a função gerar_tracos e guardar em uma lista (variável)
    lista_tracos = gerar_tracos(palavra_escolhida)

    while True:
        limpar()

        #chamar a forca para desenhar a forca 0
        desenhar_forca(contador_erro)

        #imprimo a lista de traços
        print("              ", *lista_tracos)

        #perguntar a letra e guardar em uma variavel
        letra_chutada = perguntar_letra()

        if letra_chutada not in palavra_escolhida:
            contador_erro = contador_erro + 1
            if contador_erro >= 6:
                print("Você perdeu!")
                print(f"A palavra era {palavra_escolhida}")
                break

        
        if letra_chutada in palavra_escolhida:
            contador = 0
            for letra_palavra in palavra_escolhida:
                if letra_palavra == letra_chutada:
                    lista_tracos[contador] = letra_chutada
                contador = contador + 1 

            


if __name__ == "__main__":
    jogar_forca()