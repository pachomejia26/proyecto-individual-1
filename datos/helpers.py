import pandas as pd

def getAnioPlayTimeGenre(genero):
    df = pd.read_csv('datos/dummy.csv', sep=';')
    anio = df.iloc[0][0]
    return anio.item()

def PlayTimeGenre(genero):
    df = pd.read_csv('datos/csv/merged_df.csv')
    # Filtra el DataFrame por el género especificado
    df_genero = merged_df[merged_df['genero'] == genero]

    # Agrupa por año y suma las horas jugadas
    df_agrupado = df_genero.groupby('anio')['playtime_forever'].sum().reset_index()

    # Encuentra el año con más horas jugadas
    año_con_mas_horas = df_agrupado.loc[df_agrupado['playtime_forever'].idxmax()]['anio']

    return print(f"Año de lanzamiento con más horas jugadas para {genero} : {año_con_mas_horas}")