import pandas

dicionario = {
    "estudante": ["Felipe", "Ronaldin", "Rogerin"],
    "nota": [10,9,8]
}

dataframe = pandas.DataFrame(dicionario)

for (indice,coluna) in dataframe.iterrows():
    print(coluna.nota)