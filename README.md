# proyecto-individual-1

## Documentación API

### PlayTimeGenre:

ruta: https://proyecto-gx9t.onrender.com/play-time-genre/<str:genero>/

ejemplo de petición: https://proyecto-gx9t.onrender.com/play-time-genre/action/

ejemplo de retorno: {"Anio de lanzamiento con mas horas jugadas para Genero Action": 2012}

### Recomendación 

ruta: https://proyecto-gx9t.onrender.com/recomendaciones/<str:id_producto>/

ejemplo de petición https://proyecto-gx9t.onrender.com/recomendaciones/774277/

ejemplo de retorno: {"cinco recomendaciones": [774271, 774278, 774279, 674100, 288140]}

## Bitácora procesamiento de datos

El título de cada párrafo, se refiere al nombre de los archivos ipynb.  Indico qué se hace en cada uno de ellos:

Preliminares

Leo los archivos json correspondientes a items y reviews, desanido la columnas 'reviews e items' y   los vuelvo DataFrame.  De ambos elimino la columna 'user_url', de df_user_items también elimino 'playtime_2weeks' y de df_user_reviews elimino 'funny', 'last_edited'.  Creo la columna 'sentiment_analysis' y elimino la columna 'reviews'.

Observamos que no hay valores nulos y después de borrar duplicados use_items queda con 5.094.092 filas y user_reviews con 58431

Preliminares2

Aquí nos ocupamos del archivo 'output_steam_games.json'.  Hacemos lo mismo que se hizo para los otros dos archivos pero, además, se eliminan
los NaN de las columnas 'genres','developer','realease_date','specs','price','id'.  Esta operación reduce de manera significativa el tamaño
del archivo (estos números están consigados en Preliminares2). Se hace el trabajo con la columna 'release_date' para pasarla primero a tipo date
y luego, a partir de ella, construir la columna 'anio'.  En la columna 'price' se pasan los valores tipo string a valor cero. ('Free to Play).

Para tener algo funcional, decidí de las listas que componen 'genres', quedarme con el primero que aparece entre los géneros dados en la 
documentación: Action, Adventure, Racing, Simulation, Strategy.  De esta forma cada videojuego tiene asignado un solo género.  Lo que sigue es de  df_user_items  tomar las columnas 'item_id' y 'playtime_forever', armar el DataFrame horas_jugadas y agrupando por el id conseguir el DataFrame horas_jugadas_por_juego.  Por último, se hace merge() con df_steam_games (que es donde están los géneros) y se aplica la función
año_con_mas_horas_por_genero.

EDA

CS_MODEL

Este es el código del sistema de recomendación usando la similitud del coseno

item_item_recomendation_system.json

Este es archivo que consulta la función para entregar las 5 recomendaciones.