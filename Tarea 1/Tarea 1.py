# Scarlet Rose - USACH :)

import efectivo
import impuesto

# Cuerpo del código

print('Bienvenido a EfectivoMatico 2.0')
# aquí se usa float para poder aceptar números reales, y round para convertir el número de un real a un entero
monto = round(float(input('Indique el monto que debe pagar: ')))

if monto < 1:
    print("Solo se aceptan valores positivos.")
    # Sacar al usuario del programa
    # Si pudieramos usar while, en vez de usar un assert, pediría nuevamente ingresar el monto a pagar hasta ser positivo
    assert monto > 1

if monto % 10 == 0:
    print("No le aplica la ley 20956 sobre redondeo.")

montoRedondo = efectivo.redondea(monto)
cantidadIVA = impuesto.sacaIVA(monto)

print('Según la ley 20956, usted debe pagar: $' + str(montoRedondo) + ' y de ellos $' + str(cantidadIVA) + ' corresponden al IVA.')
pago = int(input('¿Con cuanto lo pagará? '))

if pago < montoRedondo:
    print('Lamento informar que no le alcanza.')
    # Sacar al usuario del programa
    # Si pudieramos usar while, en vez de usar un assert, pediría nuevamente ingresar el pago hasta ser mayor o igual al monto redondeado
    assert pago < cantidadIVA < 0

# Redondear el vuelto a la menor decena porque no hay monedas de 5 ni de 1. Ejemplo: 20109 queda en 20100
vuelto = (pago - montoRedondo) // 10 * 10

print('Su vuelto es $' + str(vuelto))

vuelto20k = efectivo.veinteMil(vuelto)
# Si es que se entregarán más de 10 billetes, solo entregar 10
if vuelto20k > 10:
    vuelto20k = 10
# Solo imprimir el mensaje si es que habrá billetes a entregar. No se imprimirá "0 billetes de a x"
if vuelto20k > 0:
    mensaje = efectivo.mensajeBilletes(20, vuelto20k)
    print(vuelto20k, mensaje)
diferenciaVuelto = vuelto - 20000 * vuelto20k

vuelto10k = efectivo.diezMil(diferenciaVuelto)
# Si es que se entregarán más de 10 billetes, solo entregar 10
if vuelto10k > 10:
    vuelto10k = 10
# Solo imprimir el mensaje si es que habrá billetes a entregar. No se imprimirá "0 billetes de a x"
if vuelto10k > 0:
    mensaje = efectivo.mensajeBilletes(10, vuelto10k)
    print(vuelto10k, mensaje)
diferenciaVuelto = diferenciaVuelto - 10000 * vuelto10k

vuelto5k = efectivo.cincoMil(diferenciaVuelto)
# Si es que se entregarán más de 10 billetes, solo entregar 10
if vuelto5k > 10:
    vuelto5k = 10
# Solo imprimir el mensaje si es que habrá billetes a entregar. No se imprimirá "0 billetes de a x"
if vuelto5k > 0:
    mensaje = efectivo.mensajeBilletes(5, vuelto5k)
    print(vuelto5k, mensaje)
diferenciaVuelto = diferenciaVuelto - 5000 * vuelto5k

vuelto1k = efectivo.unMil(diferenciaVuelto)
# Si es que se entregarán más de 10 billetes, solo entregar 10
if vuelto1k > 10:
    vuelto1k = 10
# Solo imprimir el mensaje si es que habrá billetes a entregar. No se imprimirá "0 billetes de a x"
if vuelto1k > 0:
    mensaje = efectivo.mensajeBilletes(1, vuelto1k)
    print(vuelto1k, mensaje)
diferenciaVuelto = diferenciaVuelto - 1000 * vuelto1k

vuelto500 = efectivo.quinientos(diferenciaVuelto)
# Solo imprimir el mensaje si es que habrá monedas a entregar. No se imprimirá "0 monedas de a x"
if vuelto500 > 0:
    mensaje = efectivo.mensajeMoneda(500, vuelto500)
    print(vuelto500, mensaje)
diferenciaVuelto = diferenciaVuelto - 500 * vuelto500

vuelto100 = efectivo.cien(diferenciaVuelto)
# Solo imprimir el mensaje si es que habrá monedas a entregar. No se imprimirá "0 monedas de a x"
if vuelto100 > 0:
    mensaje = efectivo.mensajeMoneda(100, vuelto100)
    print(vuelto100, mensaje)
diferenciaVuelto = diferenciaVuelto - 100 * vuelto100

vuelto50 = efectivo.cincuenta(diferenciaVuelto)
# Solo imprimir el mensaje si es que habrá monedas a entregar. No se imprimirá "0 monedas de a x"
if vuelto50 > 0:
    mensaje = efectivo.mensajeMoneda(50, vuelto50)
    print(vuelto50, mensaje)
diferenciaVuelto = diferenciaVuelto - 50 * vuelto50

vuelto10 = efectivo.diez(diferenciaVuelto)
# Solo imprimir el mensaje si es que habrá monedas a entregar. No se imprimirá "0 monedas de a x"
if vuelto10 > 0:
    mensaje = efectivo.mensajeMoneda(10, vuelto10)
    print(vuelto10, mensaje)
diferenciaVuelto = diferenciaVuelto - 10 * vuelto10
