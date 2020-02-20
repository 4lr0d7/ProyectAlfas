#Ejercicio N1

def banco (numero):
    monto = numero*0.16
    montoTotal = numero + monto
    print (montoTotal)

n = int(input("Inserte la cantidad de Dinero:\n "))
banco(n)

#Ejercicio N2

def numMayor (num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            print("El número mayor es el 1: ",num1)
        elif num2 > num3:
            print("El número mayor es el 2: ",num2)
    else:
        print("El número mayor es el 3: ",num3)

a = float(input("Inserte el primer número: "))
b = float(input("Inserte el segundo número: "))
c = float(input("Inserte el tercer número: "))

numMayor(a, b, c)

#Ejercicio N3

def sumNum (numero):
    sumador = 0
    while numero > 0:
        varTemp = float(input("Inserte un valor: "))
        sumador = sumador + varTemp
        numero = numero - 1
    print("La suma total de los números es: ",sumador)

number = int(input("¿Cuántos números quieres poner?"))
sumNum(number)

#Ejercicio N4
def factorial (numero):
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    print(factorial)

factNumber = int(input("¿Qué número quieres escoger para saber su factorial?"))
factorial(factNumber)