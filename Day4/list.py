estados_brasil = [
    "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", 
    "Distrito Federal", "Espírito Santo", "Goiás", "Maranhão", 
    "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Pará", 
    "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro", 
    "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", 
    "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"
]

paises_america_do_sul = [
    "Argentina", "Bolívia", "Brasil", "Chile", "Colômbia", 
    "Equador", "Guiana", "Paraguai", "Peru", "Suriname", 
    "Uruguai", "Venezuela", "Guiana Francesa"
]

paises_estados = (estados_brasil, paises_america_do_sul)


estados_brasil[0] = "a"

estados_brasil.append("Mato Grosso do Norte") #adiciona um item ao final da lista
estados_brasil.extend(["Rio de Fevereiro", "Rio de Março"]) #adiciona itens ao final da lista

print(paises_estados)
    