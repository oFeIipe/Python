'''with open("weather_data.csv") as file:
    conteudo = file.readlines()
    for dado in conteudo:
        dado = dado.strip()
        dados.append(dado)

import csv

with open("weather_data.csv") as file:
    file_dados = csv.reader(file)
    temperatura = []
    for dado in file_dados:
        if dado[1] != "temp":
            temperatura.append(int(dado[1]))

print(temperatura)


import pandas
df = pandas.read_csv("weather_data.csv")
print(df['temp'])

data_dict = df.to_dict()
print(data_dict)

temperatura = df['temp'].to_list()
print(temperatura)

media = df['temp'].mean()
print(media)

maximo = df['temp'].max()
print(maximo)


print(df[df.day == "Monday"])

print(df[df.temp == df.temp.max()])

segunda = df[df.day == "Monday"]
print(segunda.condition)

def c_para_f(C):
    return (C * 9/5) + 32

temp_f = segunda.temp[0]

print(c_para_f(temp_f))'''

import pandas

df = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241016.csv")

count_gray =  len(df[df['Primary Fur Color'] == "G"])
count_red = len(df[df['Primary Fur Color'] == "Cinnamon"])
count_black = len(df[df['Primary Fur Color'] == "Black"])
novo_data_frame = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [count_gray, count_red, count_black]
}

novo = pandas.DataFrame(novo_data_frame)
#novo.to_csv("new_data.csv")

dfe = pandas.read_csv("weather_data.csv")

segunda = dfe[dfe.day == "Friday"]
print(segunda.condition)
print(dfe[dfe.temp == dfe.temp.max()])

temp_f = segunda.temp[4]

print(temp_f)