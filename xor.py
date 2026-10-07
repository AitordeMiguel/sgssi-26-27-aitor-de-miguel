def xor_cifrar(mensaje, clave):
    if len(mensaje) != len(clave):
        raise ValueError("El mensaje y la clave deben tener la misma longitud.")

    resultado = bytearray()

    for i in range(len(mensaje)):
        resultado.append(mensaje[i] ^ clave[i])

    return bytes(resultado)


# Mensaje y clave
mensaje = b"ATAQUE AL AMANECER"
clave = b"CLAVE1234567890123"

# Cifrado
criptograma = xor_cifrar(mensaje, clave)

# Descifrado: XOR con la misma clave
mensaje_descifrado = xor_cifrar(criptograma, clave)

# Mostrar resultados
print("Mensaje:             ", mensaje)
print("Mensaje hexadecimal: ", mensaje.hex())

print("Clave:               ", clave)
print("Clave hexadecimal:   ", clave.hex())

print("Criptograma:         ", criptograma)
print("Criptograma hexadecimal:", criptograma.hex())

print("Mensaje descifrado:  ", mensaje_descifrado)
print("Descifrado correcto: ", mensaje_descifrado == mensaje)
