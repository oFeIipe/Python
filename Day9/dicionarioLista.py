nested_list = ["A", "B",["C", "D"]]

print(nested_list[2][1])


diario_viagem = {
    "Brasil":{
        "cidades_visitadas": ["Belo horizonte", "São Paulo", "Rio de janeiro", "Vitória"],
        "vezes_visitado": 12 
    },
    "Portugal":{
        "cidades_visitadas": ["Benfica", "Porto", "Cristiano Ronaldo"],
        "vezes_visitado": 6 
    },
}

print(diario_viagem["Portugal"]["cidades_visitadas"][2])