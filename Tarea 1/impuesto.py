# Scarlet Rose - USACH :)

# CalculaIVA: int -> int
# Recibe un monto de dinero y retorna el 19% de ese valor
# Ejemplo: CalculaIVA(100) retorna 19
# Ejemplo: CalculaIVA(3211) retorna 610
def calculaIVA(monto):
    return round(monto * 0.19)
# Tests
assert calculaIVA(100) == 19
assert calculaIVA(3211) == 610

# SacaIVA: int -> int
# Recibe un monto de dinero y retorna el monto que corresponde al IVA.
# Ejemplo: SacaIVA(100) retorna 16
# Ejemplo: SacaIVA(3211) retorna 513
def sacaIVA(monto):
    return round(monto - monto / 1.19)
# Tests
assert sacaIVA(100) == 16
assert sacaIVA(3211) == 513