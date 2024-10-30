import pandas as pd

def exportar_data(usuario, lista_numeros, intentos, acierto_sn):
    acierto_texto = "si" if acierto_sn == 1 else "no"
    # a continuación si no tenemos nuestro excel lo crea y lo exportará a nuestro directorio
    try:
        df = pd.read_excel("Datos.xlsx")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Nombre", "Lista_numeros", "Intentos", "Acierto_Numero", "Acierto_Texto"])

    resultados = pd.DataFrame([{
        "Nombre": usuario,
        "Lista_numeros": lista_numeros,
        "Intentos": intentos,
        "Acierto_Numero": acierto_sn,
        "Acierto_Texto": acierto_texto
    }])

    df = pd.concat([df, resultados], ignore_index=True)

    df.to_excel('Datos.xlsx', index=False)


