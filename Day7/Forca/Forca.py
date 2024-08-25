import random
import img
import palavras

print(img.logo)

palavra_random = random.choice(palavras.palavras)

placeholder = ""
palavra_len = len(palavra_random)
for position in range(palavra_len):
    placeholder += "_"

game_over = False
letras_display = []
vidas = 6

print(f"{placeholder}\n")

while not game_over:
    print(f"**************************** {vidas}/6 VIDAS RESTANTES ****************************")
    letra_escolhida = input("Advinhe uma letra: ").lower()

    if letra_escolhida in letras_display:
        print(f"\nVOCÊ JÁ DIGITOU A LETRA: {letra_escolhida}, DIGITE OUTRA LETRA")

    display = ""
    
    for l in palavra_random:

        if l == letra_escolhida:
            display += l
            letras_display.append(letra_escolhida)
        elif l in letras_display:
            display += l   
        else:
            display += "_"

    if not letra_escolhida in letras_display:
        vidas -= 1
        print(f"Você escolheu: {letra_escolhida}, essa letra não está na palavra, você perde uma vida\n")

        if vidas < 1:
            print(img.estagios[vidas])
            print(f"****************** VOCÊ PERDEU! A PALAVRA CORRETA ERA: {palavra_random} *****************")               
            break
    print(display)
    print(img.estagios[vidas])
    if "_" not in display:
        game_over = True
        print("Você venceu!")
        



