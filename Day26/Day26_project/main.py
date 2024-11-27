import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
#Cria um dicionário com os valores de chave como a coluna Letra do dataFrame e o código com valor
alfabeto_otan = {coluna.letter:coluna.code for (indice,coluna) in df.iterrows()}

def funcao(word):
    try:
        #Itera sobre o dicionário de forma a procurar uma chave com o mesmo valor de um item na palavra
        lista_otan = [alfabeto_otan[i] for i in word]

    except KeyError:
        word = input("Escreva uma palavra que contenha apenas letras: ").upper()
        funcao(word)

    else:
        for codigo in lista_otan:
            print(f"Letra: {codigo[0]}, Código: {codigo}")

palavra = input("Digite uma palavra: ").upper()
funcao(palavra)