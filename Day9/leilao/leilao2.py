import img 

print(img.logo)

def maior_aposta(dicionario_pessoas):
    maior_valor = 0
    for i in dicionario_pessoas:    
        aposta = pessoa[i] # declara aposta como o valor da chave nome
        if aposta > maior_valor: # verifica o maior valor de aposta
            maior_valor = aposta # adiciona o maior valor a variavel
            nome_vencedor = i # adciona o nome da chave com a maior aposta

    print(f"A maior aposta foi ${maior_valor} O vencedor foi: {nome_vencedor}")


pessoa = {}

continucao = True

while continucao:
    print("Bem vindo ao leilão!")
    nome = input(f"Digite seu nome: ")

    valor = int(input(f"Qual sua aposta?: $"))

    pessoa[nome] = valor # declara valor como valor da chave nome

    decisao = input("\nVocê vai continuar as apostas? digite S para Sim e N para não: ").lower()
    print("\n" * 100)

    if decisao == "n":
        continucao = False
        maior_aposta(pessoa)
    else:
        continue
