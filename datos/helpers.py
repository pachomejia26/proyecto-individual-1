import pandas as pd
import json

# def getAnioPlayTimeGenre(genero):
#     df = pd.read_csv('datos/dummy.csv', sep=';')
#     anio = df.iloc[0][0]
#     return anio.item()

def getAnioPlayTimeGenre(genero):
    df = pd.read_csv('datos/csv/merged_df.csv')
    # Filtra el DataFrame por el género especificado
    df_genero = df[df['genero'] == genero]

    # Agrupa por año y suma las horas jugadas
    df_agrupado = df_genero.groupby('anio')['playtime_forever'].sum().reset_index()

    # Encuentra el año con más horas jugadas
    anio_con_mas_horas = df_agrupado.loc[df_agrupado['playtime_forever'].idxmax()]['anio']

    return anio_con_mas_horas.item()

def getRecomendaciones(id_producto):
    with open('datos/jsons/item_item_recomendation_system.json') as file:
        recomendaciones = json.load(file)
    l=[]
    for lista in recomendaciones[id_producto]:
        l.append(lista[0])
    return l    

