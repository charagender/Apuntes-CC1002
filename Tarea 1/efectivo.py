# Scarlet Rose - USACH :)

# mensajeBilletes(int, int) -> str
# Retorna "billete de x.000" o "billetes de x.000" con x siendo el valor en miles del billete,
# según si es que se dará un solo billete, o más de uno
# Ejemplos:
# mensajeBilletes(20, 1) retorna 'billete de 20.000'
# mensajeBilletes(5, 5) retorna 'billetes de 5.000'
def mensajeBilletes(mil, vuelto):
    if vuelto == 1:
        mensaje = 'billete de ' + str(mil) + '.000'
    else:
        mensaje = 'billetes de ' + str(mil) + '.000'
    return mensaje
# Test
assert mensajeBilletes(20, 1) == 'billete de 20.000'
assert mensajeBilletes(5, 5) == 'billetes de 5.000'

# mensajeMonedas(int, int) -> str
# Retorna "moneda de x" o "billetes de x" con x siendo el valor de la moneda,
# según si es que se dará una sola moneda, o más de una
# Ejemplos:
# mensajeMonedas(500, 5) retorna 'monedas de 500'
# mensajeMonedas(10, 1) retorna 'moneda de 10'
def mensajeMoneda(moneda, vuelto):
    if vuelto == 1:
        mensaje = 'moneda de ' + str(moneda)
    else:
        mensaje = 'monedas de ' + str(moneda)
    return mensaje
# Test
assert mensajeMoneda(500, 5) == 'monedas de 500'
assert mensajeMoneda(10, 1) == 'moneda de 10'

# redondea: num -> int
# Recibe un monto de dinero y debe redondearlo según el criterio de la ley 20.956
# Ejemplos:
# redondea(999) retorna 1000
# redondea(995) retorna 990 
def redondea(dinero):
    ultimo = dinero % 10
    dineroSinUltimo = dinero // 10 * 10
    if ultimo <= 5:
        dineroRedondo = dineroSinUltimo
    else:
        dineroRedondo = dineroSinUltimo + 10
    return dineroRedondo
# Tests
assert redondea(999) == 1000
assert redondea(995) == 990

# veinteMil: int -> int
# Recibe un monto de dinero y retorna la máxima cantidad de billetes de 20.000  que lo componen
# Ejemplos: 
# veinteMil(30000) retorna 1
# veinteMil(100) retorna 0
def veinteMil(monto):
    return monto // 20000
# Tests
assert veinteMil(30000) == 1
assert veinteMil(100) == 0

# diezMil: int -> int
# Recibe un monto de dinero y retorna la máxima cantidad de billetes de 10.000 que lo componen
# Ejemplos: 
# diezMil(30000) retorna 1
# diezMil(100) retorna 0
def diezMil(monto):
    return monto // 10000
# Tests
assert diezMil(40000) == 4
assert diezMil(9999) == 0

# cincoMil: int -> int
# Recibe un monto de dinero y retorna la máxima cantidad de billetes de 5.000 que lo componen
# Ejemplos: 
# cincoMil(10000) retorna 2
# cincoMil(4000) retorna 0
def cincoMil(monto):
    return monto // 5000
# Tests
assert cincoMil(10000) == 2
assert cincoMil(4000) == 0

# unMil: int -> int
# Recibe un monto de dinero y retorna la máxima cantidad de billetes de 1.000 que lo componen
# Ejemplos: 
# unMil(3000) retorna 3
# unMil(500) retorna 0
def unMil(monto):
    return monto // 1000
# Tests
assert unMil(3000) == 3
assert unMil(500) == 0

# Quinientos: int -> int
# Recibe un monto de dinero y retorna la máxima cantidad de monedas de 500 que lo componen
# Ejemplos: 
# quinientos(1501) retorna 3
# quinientos(501) retorna 1
def quinientos(monto):
    return monto // 500
# Tests
assert quinientos(1501) == 3
assert quinientos(501) == 1


# Cien: int -> int
# Recibe un monto de dinero y retorna la máxima cantidad de monedas de 100 que lo componen
# Ejemplos: 
# cien(550) retorna 5
# cien(50) retorna 0
def cien(monto):
    return monto // 100
# Tests
assert cien(550) == 5
assert cien(50) == 0

# Cincuenta: int -> int
# Recibe un monto de dinero y retorna la máxima cantidad de monedas de 50 que lo componen
# Ejemplos: 
# cincuenta(210) retorna 4
# cincuenta(152) retorna 3
def cincuenta(monto):
    return monto // 50
# Tests
assert cincuenta(210) == 4
assert cincuenta(152) == 3

# Diez: int -> int
# Recibe un monto de dinero y retorna la máxima cantidad de monedas de 10 que lo componen
# Ejemplos:
# diez(53) retorna 5
# diez(21) retorna 2
def diez(monto):
    return monto // 10
# Tests
assert diez(53) == 5
assert diez(21) == 2