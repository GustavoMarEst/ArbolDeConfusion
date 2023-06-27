import csv
import math

with open('Euc80.csv', 'r') as archivo:
    entrada = csv.reader(archivo)
    A = list(entrada)

si, no = 0, 0

for i in range(len(A)):
    if int(A[i][5]) == 1:
        si += 1
    else:
        no += 1

GT = -(si/len(A)) * (math.log2(si/len(A))) - (no/len(A)) * (math.log2(no/len(A)))
print(GT)

for j in range(1, len(A[i]) - 1):
    si_et1, si_et2, si_et3, si_et4 = 0, 0, 0, 0
    no_et1, no_et2, no_et3, no_et4 = 0, 0, 0, 0

    for i in range(len(A)):
        if int(A[i][j]) == 1:
            if int(A[i][5]) == 1:
                si_et1 += 1
            else:
                no_et1 += 1
        elif int(A[i][j]) == 2:
            if int(A[i][5]) == 1:
                si_et2 += 1
            else:
                no_et2 += 1
        elif int(A[i][j]) == 3:
            if int(A[i][5]) == 1:
                si_et3 += 1
            else:
                no_et3 += 1
        elif int(A[i][j]) == 4:
            if int(A[i][5]) == 1:
                si_et4 += 1
            else:
                no_et4 += 1

    tet1, tet2, tet3, tet4 = 0, 0, 0, 0
    tet1 = si_et1 + no_et1
    tet2 = si_et2 + no_et2
    tet3 = si_et3 + no_et3
    tet4 = si_et4 + no_et4

    Ee1, Ee2, Ee3, Ee4 = 0, 0, 0, 0

    if si_et1 != 0 and no_et1 != 0:
        Ee1 = -(si_et1 / tet1) * (math.log2(si_et1 / tet1)) - (no_et1 / tet1) * (math.log2(no_et1 / tet1))
    else:
        Ee1 = 0

    if si_et2 != 0 and no_et2 != 0:
        Ee2 = -(si_et2 / tet2) * (math.log2(si_et2 / tet2)) - (no_et2 / tet2) * (math.log2(no_et2 / tet2))
    else:
        Ee2 = 0

    if si_et3 != 0 and no_et3 != 0:
        Ee3 = -(si_et3 / tet3) * (math.log2(si_et3 / tet3)) - (no_et3 / tet3) * (math.log2(no_et3 / tet3))
    else:
        Ee3 = 0

    if si_et4 != 0 and no_et4 != 0:
        Ee4 = -(si_et4 / tet4) * (math.log2(si_et4 / tet4)) - (no_et4 / tet4) * (math.log2(no_et4 / tet4))
    else:
        Ee4 = 0

    Evar = ((tet1/len(A)) * Ee1) + ((tet2/len(A)) * Ee2) + ((tet3/len(A)) * Ee3) + ((tet4/len(A)) * Ee4)

    Gvar = abs(GT - Evar)

    rGvar = round(Gvar,4)

    a = open('EntropiasEUC80ad.txt', 'a')
    a.write(str(Ee1) + " " + str(Ee2) + " " + str(Ee3) + " " + str(Ee4) + " " + str(Evar) + " " + str(rGvar) + "\n")
    a.close()

    b = open('RespEntropiasEUC80ad.txt', 'a')
    b.write(str(si_et1) + " " + str(no_et1) + " " + str(si_et2) + " " + str(no_et2) + " " +str(si_et3) +  " " + str(no_et3) + " " + str(si_et4) + " " + str(no_et4) + "\n")
    b.close()


