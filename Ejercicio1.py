sueldos = []
nombres = []
##Funcion sueldo:
def sueldo (sal, mes):
    return sal * mes

##For de 3 empleados:
for i in range (3):
    print("")
    print("Empleado",(i+1),":")
    nombre = input("Nombre: ")
    nombres.append(nombre)
    salario = float(input("Salario mensual: "))
    meses = int(input("Meses laborados: "))
    sue = sueldo(salario, meses)
    sueldos.append(sue)
    print("Sueldo: S/.",sue)
    print("")

print("Sueldos campurados:",sueldos[:])
print("")
print("Usuario con mayor sueldo: ")
print("")
if (sueldos[0]>sueldos[1]) and (sueldos[0]>sueldos[2]):
    print("Nombre de empleado: ",nombres[0])
    print("Sueldo: S/.",sueldos[0])
elif (sueldos[1]>sueldos[0]) and (sueldos[1]>sueldos[2]):
    print("Nombre de empleado: ",nombres[1])
    print("Sueldo: S/.",sueldos[1])
else:
    print("Nombre de empleado:",nombres[2])
    print("Sueldo: S/.",sueldos[2])
print("")
