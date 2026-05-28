
import pandas as pd

#Leo los datos.

df = pd.read_csv("../datos/datos_torneo.csv")
print("DATOS DEL TORNEO")
print(df)

#Veo los equipos que participan.
equipos = set(df["equipo_local"]).union(set(df["equipo_visitante"]))

tabla = {}
for equipo in equipos:
    tabla[equipo] = {
        "PJ": 0,
        "PG": 0,
        "PE": 0,
        "PP": 0,
        "GF": 0,
        "GC": 0,
        "PTS": 0
    }

for _, fila in df.iterrows():

    local = fila["equipo_local"]
    visitante = fila["equipo_visitante"]

#Cuento partidos jugados, goles y en que condicion se jugo, si de local o visitante.
    
    gl = fila["goles_local"]
    gv = fila["goles_visitante"]
    tabla[local]["PJ"] += 1
    tabla[visitante]["PJ"] += 1
    tabla[local]["GF"] += gl
    tabla[local]["GC"] += gv

    tabla[visitante]["GF"] += gv
    tabla[visitante]["GC"] += gl

    #Guardo los resultados.
    if gl > gv:
        tabla[local]["PG"] += 1
        tabla[local]["PTS"] += 3

        tabla[visitante]["PP"] += 1

    elif gl < gv:
        tabla[visitante]["PG"] += 1
        tabla[visitante]["PTS"] += 3

        tabla[local]["PP"] += 1

    else:
        tabla[local]["PE"] += 1
        tabla[visitante]["PE"] += 1

        tabla[local]["PTS"] += 1
        tabla[visitante]["PTS"] += 1

#Creo una tabla de puntos.
tabla_df = pd.DataFrame(tabla).T
tabla_df["DG"] = tabla_df["GF"] - tabla_df["GC"]
tabla_df = tabla_df.sort_values(
    by=["PTS", "DG", "GF"],
    ascending=False
)

print("\nTABLA DE POSICIONES")
print(tabla_df)
