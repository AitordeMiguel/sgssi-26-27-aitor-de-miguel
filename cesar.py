mensaje = "Uunejvxb dw vdwmx wdnex jzdr, nw wdnbcaxb lxajixwnb"

# Palabras frecuentes en castellano
palabras_espanol = [
    "el", "la", "los", "las", "de", "del", "en", "un", "una",
    "que", "y", "es", "por", "con", "para", "se", "al", "lo"
]


def descifrar_cesar(texto, clave):
    resultado = ""

    for caracter in texto:
        if caracter.isalpha():
            posicion = ord(caracter.lower()) - ord('a')
            nueva_posicion = (posicion - clave) % 26
            nuevo_caracter = chr(ord('a') + nueva_posicion)

            if caracter.isupper():
                nuevo_caracter = nuevo_caracter.upper()

            resultado += nuevo_caracter
        else:
            resultado += caracter

    return resultado


def puntuar(texto):
    palabras = texto.lower().split()
    puntuacion = 0

    for palabra in palabras_espanol:
        if palabra in palabras:
            puntuacion += 1

    return puntuacion


mejor_clave = 0
mejor_texto = ""
mejor_puntuacion = -1

for clave in range(26):
    texto = descifrar_cesar(mensaje, clave)
    puntuacion = puntuar(texto)

    print(f"Clave {clave:2}: {texto}")

    if puntuacion > mejor_puntuacion:
        mejor_puntuacion = puntuacion
        mejor_clave = clave
        mejor_texto = texto


print("\n--- Resultado ---")
print("Clave encontrada:", mejor_clave)
print("Mensaje descifrado:", mejor_texto)
