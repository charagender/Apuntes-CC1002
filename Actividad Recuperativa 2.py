# Ejercicio Recuperativo:
# Hacer una función que verifique un RUT.
# Si el RUT es válido, debe retornar True, en caso contrario, False.

# Algoritmo para verificar un RUT:
# https://validarutchile.cl/calcular-digito-verificador.php



# largoRUT(num) -> int
# Calcular el largo de un RUT dado
# ej: largoRUT(1) == 1
# ej: largoRUT(27962409) == 8
def largoRUT(rut):
    rutSinUltimo = rut // 10
    if rutSinUltimo == 0:
        return 1
    else:
        return 1 + largoRUT(rutSinUltimo)

# Test
assert largoRUT(1) == 1    
assert largoRUT(27962409) == 8


# InvertirRUT(num) -> list[int]
# Invertir los dígitos de un RUT de derecha a izquierda
# ej: invertirRUT(1) retorna [1]
# ej: invertirRUT(27962409) retorna [9, 0, 4, 2, 6, 9, 7, 2]
def invertirRUT(rut):
    largo = largoRUT(rut)
    nuevoRUT = rut
    invertido = []
    for digito in range(0, largo):
        ultimo = nuevoRUT % 10
        invertido.append(ultimo)
        nuevoRUT = nuevoRUT // 10
    return invertido

# Test
assert invertirRUT(1) == [1]
assert invertirRUT(27962409) == [9, 0, 4, 2, 6, 9, 7, 2]


# multiplicarSumar(num) -> int
# Multiplica los dígitos individuales de un RUT que se invierte con una lista
# que se repite, y suma cada una de estas multiplicaciones
# ej: sumarDigitos(1) retorna 1
# ej: sumarDigitos(27962409) retorna 163
def multiplicarSumar(rut):
    invertido = invertirRUT(rut)
    serie = [2, 3, 4, 5, 6, 7]
    largoSerie = len(serie) - 1
    suma = item = 0
    for digito in invertido:
        if item > largoSerie:
            item = 0
        suma += digito * serie[item]
        item += 1
    return suma

# Test
assert multiplicarSumar(1) == 2
assert multiplicarSumar(27962409) == 163


# verificaRUT(num, str) -> bool
# Verifica si el dígito verificador corresponde al RUT ingresado
# ej: verificaRUT(1, 9) retorna True
# ej: verificaRUT(4013551, 1) retorna False
def verificaRUT(rut, verificador):
    digitos = [1, 2, 3, 4, 5, 6, 7, 8, 9, "K", 0]
    suma = multiplicarSumar(rut)
    sumaDiv11 = suma // 11
    divMult11 = sumaDiv11 * 11
    absoluto = abs(suma - divMult11)
    absRes11 = 11 - absoluto
    nuevoVerificador = digitos[absRes11 - 1]
    esValido = nuevoVerificador == verificador
    return esValido

# Test
assert verificaRUT(1, 9) == True
assert verificaRUT(4013551, 1) == False