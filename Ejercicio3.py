nombres = []
promedios = []

def promedio(n1, n2, n3):
    return (n1+n2+n3)/3

print("")
for i in range (5):
    print("Alumno Nº",(i+1))
    nombre = input("Nombres del alumno: ")
    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 2: "))
    nota3 = int(input("Nota 3: "))
    print("")
    prom = promedio(nota1, nota2, nota3)
    nombres.append(nombre)
    promedios.append(prom)

print("Listado de promedios: ")
print("")

muyBueno = 0

for i in range (5):
    print("Alumno ",nombres[i])
    print("Promedio ",promedios[i])
    if promedios[i]>=17:
        print("Condicion: Muy bueno")
        muyBueno = muyBueno + 1
    elif promedios[i]>=13 and promedios[i]<=16:
        print("Condicion: Bueno")
    else:
        print("Condicion: Insuficiente")
print("")
print("Cantidad de muy buenos: ",muyBueno)
print("")
