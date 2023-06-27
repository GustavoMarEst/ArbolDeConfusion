import csv
import math

def Manhattan65(x,A):
    datos = []
    resultados = []
    mp = 0
    for i in range(len(A)):
        contador = 0
        for j in range(len(A[i]) - 2):
            contador += abs(x[j] - int(A[i][j + 1]))
        resultados.append(contador)

        may = max(resultados)

    for i in range(len(A)):
        datos.append((1 - resultados[i] / may) * 100)
        if datos[i] >= 65.0:
            mp += 1

            a = open('Man65.txt', 'a')
            a.write(str(A[i][0]) + " " + str(A[i][1]) + " " + str(A[i][2]) + " " + str(A[i][3]) + " " + str(A[i][4]) + " " + str(A[i][5])  + "\n")
            a.close()

    ##print("\n",datos)
    print("El Numero De Casos Mayores Al 65% Con Manhattan Es:",mp)

def Euclidiana65(x,A):
    datos = []
    resultados = []
    mp = 0
    for i in range(len(A)):
        contador = 0
        for j in range(len(A[i]) - 2):
            contador += math.pow(x[j] - int(A[i][j + 1]), 2)
        resultados.append(math.sqrt(contador))

        may = max(resultados)

    for i in range(len(A)):
        datos.append((1 - resultados[i] / may) * 100)
        if datos[i] >= 65.0:
            mp += 1

            a = open('Euc65.txt', 'a')
            a.write(str(A[i][0]) + " " + str(A[i][1]) + " " + str(A[i][2]) + " " + str(A[i][3]) + " " + str(A[i][4]) + " " + str(A[i][5])  + "\n")
            a.close()

    ##print("\n",datos)
    print("El Numero De Casos Mayores al 65% Con Euclidiana Es:", mp)

def euclidianaNormalizada65(x,A):
    datos = []
    resultados = []
    mp = 0
    for i in range(len(A)):
        contador = 0
        for j in range(len(A[i]) - 2):
            contador += ((math.pow(x[j], 2)) - (2*(x[j] * int(A[i][j + 1]))) + (math.pow(int(A[i][j + 1]),2)))
        resultados.append(contador)

        may = max(resultados)

    for i in range(len(A)):
        datos.append((1 - resultados[i] / may) * 100)
        if datos[i] >= 65.0:
            mp += 1

            a = open('EucN65.txt', 'a')
            a.write(str(A[i][0]) + " " + str(A[i][1]) + " " + str(A[i][2]) + " " + str(A[i][3]) + " " + str(A[i][4]) + " " + str(A[i][5])  + "\n")
            a.close()

    ##print("\n",datos)
    print("El Numero De Casos Mayores 65% Con Euclidiana Norm Es:", mp)


def sorenceDice65(x,A):
    datos = []
    resultados = []
    mp = 0

    for i in range(len(A)):
        arriba = 0
        abajo = 0
        for j in range(len(A[i]) - 2):
            arriba += x[j] * int(A[i][j + 1])
            abajo += (math.pow(x[j], 2) + math.pow(int(A[i][j + 1]),2))
        resultados.append((2 * arriba) / abajo)

        may = max(resultados)

    for i in range(len(A)):
        datos.append((1 - resultados[i] / may) * 100)
        if resultados[i] >= 0.65:
            mp += 1

            a = open('Sor65.txt', 'a')
            a.write(str(A[i][0]) + " " + str(A[i][1]) + " " + str(A[i][2]) + " " + str(A[i][3]) + " " + str(A[i][4]) + " " + str(A[i][5])  + "\n")
            a.close()

    ##print("\n",datos)
    print("El Numero De Casos Mayores al 65% Con Sorence Es:", mp)

def Coseno65(x,A):
    resultados = []
    datos = []
    mp = 0

    for i in range(len(A)):
        x2 = 0
        y2 = 0
        arriba = 0
        for j in range(len(A[i]) - 2):
            arriba += x[j] * int(A[i][j + 1])
            x2 += (math.pow(x[j], 2))
            y2 += (math.pow(int(A[i][j + 1]),2))
        abajo = math.sqrt(x2 * y2)
        resultados.append(arriba/abajo)

        may = max(resultados)

    for i in range(len(A)):
        datos.append((1 - resultados[i] / may) * 100)
        if resultados[i] >= 0.65:
            mp += 1

            a = open('Cos65.txt', 'a')
            a.write(str(A[i][0]) + " " + str(A[i][1]) + " " + str(A[i][2]) + " " + str(A[i][3]) + " " + str(A[i][4]) + " " + str(A[i][5])  + "\n")
            a.close()

    ##print("\n",datos)
    print("El Numero De Casos Mayores al 65% Con Coseno Es:", mp)

def Jaccard65(x,A):
    resultados = []
    datos = []
    mp = 0

    for i in range(len(A)):
        x2 = 0
        y2 = 0
        arriba = 0
        for j in range(len(A[i]) - 2):
            arriba += x[j] * int(A[i][j + 1])
            x2 += (math.pow(x[j], 2))
            y2 += (math.pow(int(A[i][j + 1]), 2))
        abajo = x2 + y2 - arriba
        resultados.append(arriba / abajo)

        may = max(resultados)

    for i in range(len(A)):
        datos.append((1 - resultados[i] / may) * 100)
        if resultados[i] >= 0.65:
            mp += 1

            a = open('Jac65.txt', 'a')
            a.write(str(A[i][0]) + " " + str(A[i][1]) + " " + str(A[i][2]) + " " + str(A[i][3]) + " " + str(A[i][4]) + " " + str(A[i][5])  + "\n")
            a.close()

    ##print("\n",datos)
    print("El Numero De Casos Mayores al 65% Con Jaccard Es:", mp)

########################################################################################################################################################
########################################################################################################################################################
########################################################################################################################################################

def Manhattan75(x,A):
    datos = []
    resultados = []
    mp = 0
    for i in range(len(A)):
        contador = 0
        for j in range(len(A[i]) - 2):
            contador += abs(x[j] - int(A[i][j + 1]))
        resultados.append(contador)

        may = max(resultados)

    for i in range(len(A)):
        datos.append((1 - resultados[i] / may) * 100)
        if datos[i] >= 75.0:
            mp += 1

            a = open('Man75.txt', 'a')
            a.write(str(A[i][0]) + " " + str(A[i][1]) + " " + str(A[i][2]) + " " + str(A[i][3]) + " " + str(A[i][4]) + " " + str(A[i][5])  + "\n")
            a.close()

    #print("\n",datos)
    print("El Numero De Casos Mayores Al 75% Con Manhattan Es:",mp)

def Euclidiana75(x,A):
    datos = []
    resultados = []
    mp = 0
    for i in range(len(A)):
        contador = 0
        for j in range(len(A[i]) - 2):
            contador += math.pow(x[j] - int(A[i][j + 1]), 2)
        resultados.append(math.sqrt(contador))

        may = max(resultados)

    for i in range(len(A)):
        datos.append((1 - resultados[i] / may) * 100)
        if datos[i] >= 75.0:
            mp += 1

            a = open('Euc75.txt', 'a')
            a.write(str(A[i][0]) + " " + str(A[i][1]) + " " + str(A[i][2]) + " " + str(A[i][3]) + " " + str(A[i][4]) + " " + str(A[i][5])  + "\n")
            a.close()

    #print("\n",datos)
    print("El Numero De Casos Mayores Al 75% Con Euclidiana Es:", mp)

def euclidianaNormalizada75(x,A):
    datos = []
    resultados = []
    mp = 0
    for i in range(len(A)):
        contador = 0
        for j in range(len(A[i]) - 2):
            contador += ((math.pow(x[j], 2)) - (2*(x[j] * int(A[i][j + 1]))) + (math.pow(int(A[i][j + 1]),2)))
        resultados.append(contador)

        may = max(resultados)

    for i in range(len(A)):
        datos.append((1 - resultados[i] / may) * 100)
        if datos[i] >= 75.0:
            mp += 1

            a = open('EucN75.txt', 'a')
            a.write(str(A[i][0]) + " " + str(A[i][1]) + " " + str(A[i][2]) + " " + str(A[i][3]) + " " + str(A[i][4]) + " " + str(A[i][5])  + "\n")
            a.close()

    #print("\n",datos)
    print("El Numero De Casos Mayores Al 75% Con Euclidiana Norm Es:", mp)


def sorenceDice75(x,A):
    datos = []
    resultados = []
    mp = 0

    for i in range(len(A)):
        arriba = 0
        abajo = 0
        for j in range(len(A[i]) - 2):
            arriba += x[j] * int(A[i][j + 1])
            abajo += (math.pow(x[j], 2) + math.pow(int(A[i][j + 1]),2))
        resultados.append((2 * arriba) / abajo)

        may = max(resultados)

    for i in range(len(A)):
        datos.append((1 - resultados[i] / may) * 100)
        if resultados[i] >= 0.75:
            mp += 1

            a = open('Sor75.txt', 'a')
            a.write(str(A[i][0]) + " " + str(A[i][1]) + " " + str(A[i][2]) + " " + str(A[i][3]) + " " + str(A[i][4]) + " " + str(A[i][5])  + "\n")
            a.close()

    #print("\n",datos)
    print("El Numero De Casos Mayores Al 75% Con Sorence Es:", mp)

def Coseno75(x,A):
    resultados = []
    datos = []
    mp = 0

    for i in range(len(A)):
        x2 = 0
        y2 = 0
        arriba = 0
        for j in range(len(A[i]) - 2):
            arriba += x[j] * int(A[i][j + 1])
            x2 += (math.pow(x[j], 2))
            y2 += (math.pow(int(A[i][j + 1]),2))
        abajo = math.sqrt(x2 * y2)
        resultados.append(arriba/abajo)

        may = max(resultados)

    for i in range(len(A)):
        datos.append((1 - resultados[i] / may) * 100)
        if resultados[i] >= 0.75:
            mp += 1

            a = open('Cos75.txt', 'a')
            a.write(str(A[i][0]) + " " + str(A[i][1]) + " " + str(A[i][2]) + " " + str(A[i][3]) + " " + str(A[i][4]) + " " + str(A[i][5])  + "\n")
            a.close()

    #print("\n",datos)
    print("El Numero De Casos Mayores Al 75% Con Coseno Es:", mp)

def Jaccard75(x,A):
    resultados = []
    datos = []
    mp = 0

    for i in range(len(A)):
        x2 = 0
        y2 = 0
        arriba = 0
        for j in range(len(A[i]) - 2):
            arriba += x[j] * int(A[i][j + 1])
            x2 += (math.pow(x[j], 2))
            y2 += (math.pow(int(A[i][j + 1]), 2))
        abajo = x2 + y2 - arriba
        resultados.append(arriba / abajo)

        may = max(resultados)

    for i in range(len(A)):
        datos.append((1 - resultados[i] / may) * 100)
        if resultados[i] >= 0.75:
            mp += 1

            a = open('Jac75.txt', 'a')
            a.write(str(A[i][0]) + " " + str(A[i][1]) + " " + str(A[i][2]) + " " + str(A[i][3]) + " " + str(A[i][4]) + " " + str(A[i][5])  + "\n")
            a.close()

    #print("\n",datos)
    print("El Numero De Casos Mayores al 75% Con Jaccard Es:", mp)

########################################################################################################################################################
########################################################################################################################################################
########################################################################################################################################################

def Manhattan80(x,A):
    datos = []
    resultados = []
    mp = 0
    for i in range(len(A)):
        contador = 0
        for j in range(len(A[i]) - 2):
            contador += abs(x[j] - int(A[i][j + 1]))
        resultados.append(contador)

        may = max(resultados)

    for i in range(len(A)):
        datos.append((1 - resultados[i] / may) * 100)
        if datos[i] >= 80.0:
            mp += 1

            a = open('Man80.txt', 'a')
            a.write(str(A[i][0]) + " " + str(A[i][1]) + " " + str(A[i][2]) + " " + str(A[i][3]) + " " + str(A[i][4]) + " " + str(A[i][5])  + "\n")
            a.close()

    #print("\n",datos)
    print("El Numero De Casos Mayores Al 80% Con Manhattan Es:",mp)

def Euclidiana80(x,A):
    datos = []
    resultados = []
    mp = 0
    for i in range(len(A)):
        contador = 0
        for j in range(len(A[i]) - 2):
            contador += math.pow(x[j] - int(A[i][j + 1]), 2)
        resultados.append(math.sqrt(contador))

        may = max(resultados)

    for i in range(len(A)):
        datos.append((1 - resultados[i] / may) * 100)
        if datos[i] >= 80.0:
            mp += 1

            a = open('Euc80.txt', 'a')
            a.write(str(A[i][0]) + " " + str(A[i][1]) + " " + str(A[i][2]) + " " + str(A[i][3]) + " " + str(A[i][4]) + " " + str(A[i][5])  + "\n")
            a.close()

    #print("\n",datos)
    print("El Numero De Casos Mayores Al 80% Con Euclidiana Es:", mp)

def euclidianaNormalizada80(x,A):
    datos = []
    resultados = []
    mp = 0
    for i in range(len(A)):
        contador = 0
        for j in range(len(A[i]) - 2):
            contador += ((math.pow(x[j], 2)) - (2*(x[j] * int(A[i][j + 1]))) + (math.pow(int(A[i][j + 1]),2)))
        resultados.append(contador)

        may = max(resultados)

    for i in range(len(A)):
        datos.append((1 - resultados[i] / may) * 100)
        if datos[i] >= 80.0:
            mp += 1

            a = open('EucN80.txt', 'a')
            a.write(str(A[i][0]) + " " + str(A[i][1]) + " " + str(A[i][2]) + " " + str(A[i][3]) + " " + str(A[i][4]) + " " + str(A[i][5])  + "\n")
            a.close()

    #print("\n",datos)
    print("El Numero De Casos Mayores Al 80% Con Euclidiana Norm Es:", mp)


def sorenceDice80(x,A):
    datos = []
    resultados = []
    mp = 0

    for i in range(len(A)):
        arriba = 0
        abajo = 0
        for j in range(len(A[i]) - 2):
            arriba += x[j] * int(A[i][j + 1])
            abajo += (math.pow(x[j], 2) + math.pow(int(A[i][j + 1]),2))
        resultados.append((2 * arriba) / abajo)

        may = max(resultados)

    for i in range(len(A)):
        datos.append((1 - resultados[i] / may) * 100)
        if resultados[i] >= 0.80:
            mp += 1

            a = open('Sor80.txt', 'a')
            a.write(str(A[i][0]) + " " + str(A[i][1]) + " " + str(A[i][2]) + " " + str(A[i][3]) + " " + str(A[i][4]) + " " + str(A[i][5])  + "\n")
            a.close()

    #print("\n",datos)
    print("El Numero De Casos Mayores Al 80% Con Sorence Es:", mp)

def Coseno80(x,A):
    resultados = []
    datos = []
    mp = 0

    for i in range(len(A)):
        x2 = 0
        y2 = 0
        arriba = 0
        for j in range(len(A[i]) - 2):
            arriba += x[j] * int(A[i][j + 1])
            x2 += (math.pow(x[j], 2))
            y2 += (math.pow(int(A[i][j + 1]),2))
        abajo = math.sqrt(x2 * y2)
        resultados.append(arriba/abajo)

        may = max(resultados)

    for i in range(len(A)):
        datos.append((1 - resultados[i] / may) * 100)
        if resultados[i] >= 0.80:
            mp += 1

            a = open('Cos80.txt', 'a')
            a.write(str(A[i][0]) + " " + str(A[i][1]) + " " + str(A[i][2]) + " " + str(A[i][3]) + " " + str(A[i][4]) + " " + str(A[i][5])  + "\n")
            a.close()

    #print("\n",datos)
    print("El Numero De Casos Mayores Al 80% Con Coseno Es:", mp)

def Jaccard80(x,A):
    resultados = []
    datos = []
    mp = 0

    for i in range(len(A)):
        x2 = 0
        y2 = 0
        arriba = 0
        for j in range(len(A[i]) - 2):
            arriba += x[j] * int(A[i][j + 1])
            x2 += (math.pow(x[j], 2))
            y2 += (math.pow(int(A[i][j + 1]), 2))
        abajo = x2 + y2 - arriba
        resultados.append(arriba / abajo)

        may = max(resultados)

    for i in range(len(A)):
        datos.append((1 - resultados[i] / may) * 100)
        if resultados[i] >= 0.80:
            mp += 1

            a = open('Jac80.txt', 'a')
            a.write(str(A[i][0]) + " " + str(A[i][1]) + " " + str(A[i][2]) + " " + str(A[i][3]) + " " + str(A[i][4]) + " " + str(A[i][5])  + "\n")
            a.close()

    #print("\n",datos)
    print("El Numero De Casos Mayores Al 80% Con Jaccard Es:", mp)


########################################################################################################################################################
########################################################################################################################################################
########################################################################################################################################################

x = [2, 3, 1, 4]
lista = []

with open('datosvalvula.csv', 'r') as archivo:
    entrada = csv.reader(archivo)
    A = list(entrada)

print("\nCASOS MAYORES AL 65%")
Manhattan65(x,A)
Euclidiana65(x,A)
euclidianaNormalizada65(x,A)
sorenceDice65(x,A)
Coseno65(x,A)
Jaccard65(x,A)

print("\nCASOS MAYORES AL 75%")
Manhattan75(x,A)
Euclidiana75(x,A)
euclidianaNormalizada75(x,A)
sorenceDice75(x,A)
Coseno75(x,A)
Jaccard75(x,A)

print("\nCASOS MAYORES AL 80%")
Manhattan80(x,A)
Euclidiana80(x,A)
euclidianaNormalizada80(x,A)
sorenceDice80(x,A)
Coseno80(x,A)
Jaccard80(x,A)