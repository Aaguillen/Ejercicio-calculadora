0=0
while 0!=5:

print("Calculadora")

print("----------------")

prit("Menu")

print("1. Suma")

print("2. Resta")

print("3. Multiplicacion")

print("4. Division")

print("5. Salir")

    0=int(input("seleccione una opcion:"))

      if 0==1:

        suma()

      elif 0==2:
    
        resta()

      elif 0==3:

        multiplicacion()

      elif 0==4:

        division

      elif 0==5:
        
        break

def suma ():

    num1=int(input("introduce un numero:"))
    num2=int(input("introduce un numero:"))

      suma = num1+num2
      print("el resultado de la suma es:", suma)

def resta ():

    num1=int(input("introduce un numero:"))
    num2=int(input("introduce un numero:"))

      resta = num1-num2
      print("el resultado de la resta es:", resta)

def multiplicacion ():

    num1=int(input("introduce un numero:"))
    num2=int(input("introduce un numero:"))

      multiplicacion = num1*num2
      print("el resultado de la multiplicacion es:", multiplicacion)

def division ():

    num1=int(input("introduce un numero:"))
    num2=int(input("introduce un numero:"))

      division = num1/num2
      print("el resultado de la division es:", division)

