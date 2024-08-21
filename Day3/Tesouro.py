print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************''')


print("\nBem vindo a ilha do tesouro")

escolha1 = input("""\nVocê chegou à entrada de uma caverna escura, onde o tesouro está supostamente escondido. À sua frente, há dois caminhos:
\nEsquerda: Seguir pelo túnel à esquerda, que é estreito e parece seguro, mas você ouve um som estranho vindo de lá.
Direita: Seguir pelo túnel à direita, que é mais largo e iluminado por uma luz fraca ao longe.

Esquerda ou Direita? """).lower()

if escolha1 == "direita":
    print("""\n\n\nVocê segue pelo túnel à direita. A luz fraca começa a aumentar conforme você avança, revelando inscrições antigas nas paredes. Você foi no caminho certo e pode continuar a busca pelo tesouro. """)
    escolha2 = input("""Após andar pelo túnel iluminado, você chega a uma grande caverna com um abismo no meio. Uma velha ponte de corda balança com o vento,e ao lado há uma passagem estreita nas laterais da caverna.
                     \nEsquerda: Atravesse a ponte de corda, mesmo parecendo frágil, pois é o caminho mais rápido.
Direita: Use a passagem estreita ao longo da lateral da caverna, que parece ser mais segura, mas demorará mais.
                     \nEsqueda ou Direita? """).lower()
    


    if escolha2 == "esquerda":
        print("Você escolhe ir pra esquerda e atravessar a ponte de corda. À medida que você caminha, a ponte começa a ranger e balançar violentamente. De repente, uma das cordas principais se solta, e você cai no abismo. Game Over.")        
    else:
         print("Você decide usar a passagem a direita estreita da lateral da caverna. Embora demore mais, você consegue evitar a ponte perigosa e, após alguns minutos, chega ao outro lado em segurança.")
         escolha3=input("""Você finalmente chega ao salão onde o tesouro está guardado. À sua frente, há três cofres antigos, um de ouro e outro de pedra outro de Rubi. 
                        \nCofre de Ouro: Abrir o cofre de ouro, que brilha intensamente e parece conter grandes riqueza. 
Cofre de Pedra: Abrir o cofre de pedra, que é simples e desgastado pelo tempo, mas está coberto de inscrições misteriosas.
Cofre de Rubi: Abrir o cofre de Rubi, que é brilhante e parece mistico
                        \nQual Baú você escolhe? """).lower()
         
         



         if escolha3 == "ouro":
                  print("Você abre o Baú de ouro, mas logo que o faz, uma armadilha é acionada. O chão se abre, e você cai em uma câmara secreta cheia de areia movediça. Game Over.")
         elif escolha3 == "rubi":
                  print("Você abre o Baú de Rubi, mas percebe que se tratava de uma armadilha, flechas são disparadas em você e te perfuram. Game Over.") 
         else:
                  print("Você escolhe abrir o Baú de pedra. Dentro, você encontra o verdadeiro tesouro, protegido por séculos e intacto. Parabéns! Você encontrou o tesouro e completou a missão. Você venceu!")           
           
            
        
else:
    print("\nVocê decide seguir pelo túnel estreito à esquerda. Enquanto avança, o som estranho se intensifica até que você percebe que são morcegos! Eles se assustam com sua presença e começam a voar em sua direção. Infelizmente, você é forçado a voltar e acaba se perdendo na escuridão. Game Over.")
        