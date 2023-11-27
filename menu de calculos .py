import math

def Suma_numeros():
        N = int(input("Proporcione la cantidad de números a sumar: "))
        plus = 0
        for i in range(N):
         numero = float(input(f"Ingrese el número {i + 1}: "))
         plus += numero
        print("La suma de los números es:", plus)

def prod_num():
     numeros = int(input("Teclee la cantidad de numeros que desea multiplicar: "))
     product = 1
     for i in range(numeros):
          digito = float(input(f"Teclee el numero deseado {i + 1}: "))
          product *= digito 
          print("El producto de los numeros es: ", product)

def division():
     numero1 = float(input("Ingrese el digito numerador:"))
     numero2 = float(input("Ingrese el digito denominador: "))
     if numero2 != 0:
          resultado = numero1/numero2
          print("Resultado de la division: ",resultado)
     else: 
          print("*Error*")

def Factorial():
     x = int(input("Teclee el numero para calcular el factorial"))
     facto = math.factorial(x)
     print(f"El factorial de {x} es : {facto}")

def Tablas_Multi():
     tabla = int(input("proporcione la tabla de multiplicar."))
     for i in range(1,11):
      print(f"{Tablas_Multi} x {i} = {Tablas_Multi * i}")

def calculo_cuadrado_cubo():
     num = float(input("Proporcione un numero para calcular su cuadrado y cubo:"))
     cuadrado=num **2
     cubo = num ** 3
     print(f"El cuadrado de {num}es: {cuadrado}")
     print(f"El ubo de {num} es: {cubo}")

def Promedios():
     numeros = []
     while True :
          numero = float(input("Ingrese un numero (o -1 para salir)"))
          if numero == -1:
               break
          numeros.append(numero)
          if numeros :
               prom = sum(numeros) / len(numeros)
               print("El promedio es :", Promedios)
          else:
               print("**Error**")

def Max_Min():
     x = int(input("Teclee los numeros a comparar: "))
     if x>0:
          numeros = [int(input(f"Ingrese el número {i + 1}: ")) for i in range(x)]
          maximo = max(numeros)
          minimo = min(numeros)
          print (f"Maximo :{maximo}")
          print(f"Minimo: {minimo}")
          print(f"Se ingresaron {x} valores.")
     else:
          print("**error**")
while True:
    print("\nMenú de opciones:")
    print("1. Suma de n números")
    print("2. Producto entre n números")
    print("3. División entre 2 números")
    print("4. Calcular factorial")
    print("5. Tablas de multiplicar")
    print("6. Cuadrado y cubo de un número")
    print("7. Promedio de una serie de números")
    print("8. Máximo y mínimo de n números")
    print("0. Salir")
    
    Opciones=input("Selecciona una opcion")   
    if Opciones == "1":
        Suma_numeros()
    elif Opciones == "2":
        prod_num()
    elif Opciones == "3":
        division()
    elif Opciones == "4":
        Factorial()
    elif Opciones == "5":
        Tablas_Multi()
    elif Opciones == "6":
        calculo_cuadrado_cubo()
    elif Opciones == "7":
        Promedios()
    elif Opciones == "8":
        Max_Min()
    elif Opciones == "0":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")

    
