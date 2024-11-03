import random

nomes = ["Alex", "Beth", "Caroline", "David", "Eleonora", "Felipão"]

dicionario = {estudante:random.randint(1,100) for estudante in nomes}


dicionario_alunos_aprovados = {estudante:nota for (estudante,nota) in dicionario.items() if nota >= 60}

print(dicionario)
print(dicionario_alunos_aprovados)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {palavra:len(palavra) for palavra in sentence.split()}
print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {dia:(temp * 9/5) + 32 for (dia,temp) in weather_c.items()}

print(weather_f)