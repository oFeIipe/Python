with open('input/Letters/starting_letter.txt') as conteudo_carta:
    carta = conteudo_carta.read()

    with open('input/Names/invited_names.txt') as conteudo_nomes:
        nomes = conteudo_nomes.readlines()
        for nome in nomes:
            nome = nome.strip()
            with open(f"output/ReadyToSend/carta_para_{nome}.txt", "w") as cartas_prontas:
                x = carta.replace('[name]', f"{nome}")
                cartas_prontas.write(x)