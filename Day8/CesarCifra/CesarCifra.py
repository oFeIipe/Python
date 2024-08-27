import img

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(img.logo)
def caesar(direction, texto_original, shift_total): #Define a função e os paramêtros
    texto_saida = ""

    if direction == "decode": # Se direction for igual a decode decrementa shift
            shift_total *= -1  

    for i in texto_original:         
        if i.isalpha():
            shift_position = alfabeto.index(i) + shift_total # Verifica a posição de cada letra do alfabeto mais o shift_total e armazena em uma variável
            shift_position %= len(alfabeto) # Mantém shift_position em um valor válido, idenpendente quantas vezes a lista é percorrida
            texto_saida += alfabeto[shift_position]# Adiciona letra por letra no texto de saida, com base na posição da letra + ou - shift
        else:
             texto_saida += i    # Se a i não for uma letra ela será adcionada na palavra final sem alterações
    print(f"\nA mensagem {direction} é: {texto_saida}\n") 
  

while True: # executa o código principal enquanto for True

    direcao = input("\nDigite decode para decodificar uma palavra, ou encode para codificar uma palavra: ").lower()
    texto = input("\nDigite sua menssagem: ").lower()
    shift = int(input("Type the shift number: "))

    caesar(texto_original=texto, shift_total=shift, direction=direcao) # chama a função e os paramêtros

    resposta = input("Você quer continuar? digite Sim ou Não: ").lower() 

    if resposta == "nao" or resposta == "não": # caso o usuário digite não o programa será encerrado
        break