def format_nome(p_nome,s_nome):
    if p_nome == "" or s_nome == "":
        return "Nome ou Sobrenome pendente"
    s_nome_f = s_nome.title()
    p_nome_f = p_nome.title()
    return f"{p_nome_f} {s_nome_f}"

print(format_nome(input("Digite seu primeiro nome: "), input("Digite seu sobrenome: ")))