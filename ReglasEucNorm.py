import csv

with open('datosvalvula.csv', 'r') as archivo:
    entrada = csv.reader(archivo)
    A = list(entrada)

vp, vn, fp, fn = 0, 0, 0, 0

#EUCLIDIANA NORMALIZADA 65
"""for i in range(300):
    if int(A[i][1]) == 2 or int(A[i][1]) == 3:
        if int(A[i][5]) == 2:
            fp += 1
        else:
            fn += 1
    elif int(A[i][1]) == 4:
        if int(A[i][5]) == 1:
            vp += 1
        else:
            vn += 1
    elif int(A[i][1]) == 1:
        if int(A[i][2]) == 1 or int(A[i][2]) == 2:
            if int(A[i][5]) == 2:
                fp += 1
            else:
                fn += 1
        elif int(A[i][2]) == 3:
            if int(A[i][3]) == 1 or int(A[i][3]) == 2:
                if int(A[i][5]) == 2:
                    fp += 1
                else:
                    fn += 1
            elif int(A[i][3]) == 3:
                if int(A[i][4]) == 1:
                    if int(A[i][5]) == 1:
                        vp += 1
                    else:
                        vn += 1
                elif int(A[i][4]) == 2 or int(A[i][4]) == 3 or int(A[i][4]) == 4:
                    if int(A[i][5]) == 2:
                        fp += 1
                    else:
                        fn += 1"""

#EUCLIDIANA NORMALIZADA 75
"""for i in range(300):
    if int(A[i][2]) == 2:
        if int(A[i][5]) == 2:
            fp += 1
        else:
            fn += 1
    elif int(A[i][2]) == 3:
        if int(A[i][5]) == 1:
            vp += 1
        else:
            vn += 1
    elif int(A[i][2]) == 1:
        if int(A[i][1]) == 2 or int(A[i][1]) == 3:
            if int(A[i][5]) == 2:
                fp += 1
            else:
                fn += 1
        elif int(A[i][1]) == 4:
            if int(A[i][5]) == 1:
                vp += 1
            else:
                vn += 1
        elif int(A[i][1]) == 1:
            if int(A[i][3]) == 1:
                if int(A[i][5]) == 2:
                    fp += 1
                else:
                    fn += 1
            elif int(A[i][3]) == 3:
                if int(A[i][5]) == 1:
                    vp += 1
                else:
                    vn += 1
            elif int(A[i][3]) == 2:
                if int(A[i][4]) == 1 or int(A[i][4]) == 2:
                    if int(A[i][5]) == 1:
                        vp += 1
                    else:
                        vn += 1
                elif int(A[i][4]) == 3 or int(A[i][4]) == 4:
                    if int(A[i][5]) == 2:
                        fp += 1
                    else:
                        fn += 1"""

#EUCLIDIANA NORMALIZADA 80
"""for i in range(300):
    if int(A[i][1]) == 1 or int(A[i][1]) == 3 or int(A[i][1]) == 4:
        if int(A[i][5]) == 2:
            fp += 1
        else:
            fn += 1
    elif int(A[i][1]) == 2:
        if int(A[i][2]) == 2 or int(A[i][2]) == 3:
            if int(A[i][5]) == 2:
                fp += 1
            else:
                fn += 1
        elif int(A[i][2]) == 1:
            if int(A[i][3]) == 1 or int(A[i][3]) == 3:
                if int(A[i][5]) == 2:
                    fp += 1
                else:
                    fn += 1
            elif int(A[i][3]) == 2:
                if int(A[i][4]) == 1 or int(A[i][4]) == 2:
                    if int(A[i][5]) == 1:
                        vp += 1
                    else:
                        vn += 1
                elif int(A[i][4]) == 3 or int(A[i][4]) == 4:
                    if int(A[i][5]) == 2:
                        fp += 1
                    else:
                        fn += 1"""


val = vn + vp + fn + fp
print(val)

p = vp / (vp + fp);
print(p);

r = vp / (vp + fn);
print(r);

f1 = (2 * (r * p)) / (r + p);
print(f1);