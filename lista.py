lista_animais = ["cavalo", "onitorrinco", "pato", "tamanduá"]

print(*lista_animais)

lista_animais.append("gato") #acrescenta um item

print(*lista_animais)

lista_animais.remove("pato") #remover um item

print(*lista_animais)

lista_animais[1]= "Perry" #substitui o item, lembrando que se inicia a numeração com 0

print(*lista_animais)

print(*lista_animais[2]) #imprime apenas o item 2 e de forma soletrada espaçadas por conta do *

for animal in lista_animais:  #o "for" é o lopping da lista, percorrer a lista
        if animal == "Perry":
                print("Oh não é Perry o ornitorrinco!!!")
        else:
            print(f"Eu amo {animal}")
