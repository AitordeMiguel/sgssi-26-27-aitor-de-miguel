from collections import Counter


mensaje = """RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.

AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."""


def obtener_palabras(texto):
    palabras = []
    palabra = ""

    for caracter in texto:
        if caracter.isalpha():
            palabra += caracter
        else:
            if palabra:
                palabras.append(palabra)
                palabra = ""

    if palabra:
        palabras.append(palabra)

    return palabras


def mostrar_frecuencias():
    letras = [
        caracter
        for caracter in mensaje.upper()
        if caracter.isalpha()
    ]

    contador = Counter(letras)
    total = len(letras)

    print("\n--- FRECUENCIA DE LETRAS ---")

    for letra, cantidad in contador.most_common():
        porcentaje = cantidad / total * 100
        barra = "█" * int(porcentaje)

        print(
            f"{letra}: {cantidad:3} "
            f"({porcentaje:5.2f}%) {barra}"
        )


def mostrar_palabras():
    palabras = obtener_palabras(mensaje)

    print("\n--- PALABRAS DE 1, 2 Y 3 LETRAS ---")

    for longitud in [1, 2, 3]:
        contador = Counter(
            palabra.upper()
            for palabra in palabras
            if len(palabra) == longitud
        )

        print(f"\nPalabras de {longitud} letra(s):")

        if contador:
            for palabra, cantidad in contador.most_common():
                print(f"  {palabra} ({cantidad} veces)")
        else:
            print("  Ninguna")


def mostrar_repeticiones():
    palabras = obtener_palabras(mensaje)

    contador = Counter(
        palabra.upper()
        for palabra in palabras
        if len(palabra) >= 2
    )

    print("\n--- PALABRAS REPETIDAS ---")

    repetidas = False

    for palabra, cantidad in contador.most_common():
        if cantidad > 1:
            print(f"{palabra}: {cantidad} veces")
            repetidas = True

    if not repetidas:
        print("No hay palabras repetidas.")


def descifrar(texto, sustituciones):
    resultado = ""

    for caracter in texto:

        # Las minúsculas ya están descifradas.
        # Se mantienen exactamente igual.
        if caracter.islower():
            resultado += caracter

        # Las mayúsculas siguen cifradas.
        elif caracter.isupper():

            if caracter in sustituciones:
                resultado += sustituciones[caracter].lower()
            else:
                resultado += caracter

        # Espacios, signos, números, etc.
        else:
            resultado += caracter

    return resultado


def mostrar_sustituciones(sustituciones):
    print("\n--- SUSTITUCIONES ACTUALES ---")

    if not sustituciones:
        print("No hay sustituciones.")
        return

    for cifrada, descifrada in sorted(sustituciones.items()):
        print(f"{cifrada} -> {descifrada}")


sustituciones = {}


print("=== ATAQUE POR SUSTITUCIÓN ===")
print()
print("Mayúsculas = todavía cifrado")
print("Minúsculas = ya descifrado")
print()
print("Comandos disponibles:")
print("  frecuencia       -> mostrar frecuencia de letras")
print("  palabras         -> mostrar palabras de 1, 2 y 3 letras")
print("  repetidas        -> mostrar palabras repetidas")
print("  texto            -> mostrar el texto actual")
print("  sustituciones    -> mostrar sustituciones realizadas")
print("  X Y              -> sustituir X por Y")
print("  borrar X         -> eliminar la sustitución de X")
print("  salir             -> terminar el programa")


while True:

    comando = input("\n> ").strip()

    if not comando:
        continue

    if comando.lower() == "salir":
        print("Programa terminado.")
        break

    elif comando.lower() == "frecuencia":
        mostrar_frecuencias()

    elif comando.lower() == "palabras":
        mostrar_palabras()

    elif comando.lower() == "repetidas":
        mostrar_repeticiones()

    elif comando.lower() == "texto":
        print("\n--- TEXTO ACTUAL ---")
        print(descifrar(mensaje, sustituciones))

    elif comando.lower() == "sustituciones":
        mostrar_sustituciones(sustituciones)

    elif comando.lower().startswith("borrar "):
        partes = comando.split()

        if (
            len(partes) == 2
            and len(partes[1]) == 1
            and partes[1].isupper()
            and partes[1].isalpha()
        ):
            letra = partes[1]

            if letra in sustituciones:
                del sustituciones[letra]
                print(f"Sustitución de {letra} eliminada.")
            else:
                print(f"No existe una sustitución para {letra}.")

        else:
            print("Uso: borrar X (X debe ser mayúscula)")

    else:
        partes = comando.split()

        if len(partes) == 2 and len(partes[0]) == 1 and len(partes[1]) == 1:

            cifrada = partes[0]
            descifrada = partes[1]

            # La letra cifrada DEBE ser mayúscula.
            if not cifrada.isalpha() or not cifrada.isupper():
                print("La letra cifrada debe escribirse en MAYÚSCULA.")
                print("Ejemplo: V Y")

            # La letra descifrada puede escribirse en mayúscula
            # o minúscula; internamente se guarda en minúscula.
            elif not descifrada.isalpha():
                print("La letra descifrada debe ser una letra.")

            else:
                descifrada = descifrada.lower()

                sustituciones[cifrada] = descifrada

                print(
                    f"Sustitución añadida: "
                    f"{cifrada} -> {descifrada}"
                )

                print("\n--- TEXTO ACTUAL ---")
                print(descifrar(mensaje, sustituciones))

        else:
            print("Comando no reconocido.")
            print("Escribe 'frecuencia', 'palabras', 'repetidas',")
            print("'texto', 'sustituciones', 'borrar X' o 'salir'.")
