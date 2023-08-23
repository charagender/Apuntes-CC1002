# largoNumero(int -> int)
# contar cuántos dígitos tiene un número dado
# ej: largoNumero(2332) retorna 4
def largoNumero(numero):
    numeroSinUltimo = numero // 10
    if (numeroSinUltimo == 0):
        return 1
    else:
        return 1 + largoNumero(numeroSinUltimo)

# Test
assert largoNumero(2332) == 4

# invertirNatural(int -> int
# Invierte los dígitos de un número dado
# ej: invertirNatural(4321) retorna 1234
# ej: invertirNatural(3211) retorna 1123
def invertirNatural(numero):
    if(numero // 10 == 0):
        return numero
    else:
        ultimo = numero % 10
        numeroSinUltimo = numero // 10
        return ultimo * 10**(largoNumero(numeroSinUltimo)) + invertirNatural(numeroSinUltimo)

# Test
assert invertirNatural(4321) == 1234
assert invertirNatural(3211) == 1123

# esPalindromo(int -> bool)
# Te dice si un número dado es políndromo o no
# ej: esPalindromo(3443) retorna True
# ej: esPalindromo(4322) retorna False
def esPalindromo(numero):
    return numero == invertirNatural(numero)

# Test
assert esPalindromo(3443)
assert not esPalindromo(4332)