def calculate_love_score(name1, name2):
    letras_true = ["t","r","u","e","T","R","U","E"]
    letras_love = ["l","o","v","e","L","O","V","E"]
    total_true = 0
    total_love = 0
    
    for char in name1 + name2:
        if char in letras_true:
            total_true += 1
    print(f"total = {total_true}")
    for char in name1 + name2:
        if char in letras_love:
            total_love += 1
    print(f"total = {total_love}")
    total = int(str(total_true)+str(total_love))
    print(total)

    

calculate_love_score("Kanye West", "Kim Kardashian")

'''def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower() #Converte os nomes unidos para lower case
    
    t = lower_names.count("t")  #conta a quantidade de letras escolhidas
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e  #soma o valor dessas letras
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    
    
    score = int(str(first_digit) + str(second_digit))  #Converte as contas para string
    print(score)                                       #para que assim elas possam ser concatenadas 
    
calculate_love_score("Kanye West", "Kim Kardashian")  #Recebe o valor dos argumentos''' 