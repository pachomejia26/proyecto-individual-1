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

def UserForGenre(genero):
    df1 = pd.read_parquet('datos/csv/df_user_items4.parquet')
    df2 = pd.read_csv('datos/csv/df_steam_games_25k.csv')
    # unimos los dataframe:
    merged_df1 = pd.merge(df1, df2, on='id')

    #filtramos por genero:
    # Paso 2: Filtrar por género
    filtered_df = merged_df1[merged_df1['genero'] == genero]

     #  Encontrar el jugador que más jugó por año
    result = filtered_df.groupby(['anio', 'id'])['playtime_forever'].sum().reset_index()
    result = result.sort_values(by='playtime_forever', ascending=False).drop_duplicates(subset='anio')

    return result


