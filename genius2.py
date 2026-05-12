import os
import time

dicionario

def limpar_tela():
    os.system("color 07")
    os.system("cls")

def mudar_cor(cor): # para criar um parâmetro é só colocar dentro do ()
    os.system(f"color {cor}")
    time.sleep(1)
    limpar_tela()

mudar_cor(80)
mudar_cor(70)
mudar_cor(30)
mudar_cor(10)

