##Definimos las funciones para cada caso
def perimetro (lado):
    return lado * 4
def area (lado):
    return lado ** 2
print("")
##Pedimos el lado del cuadrado
lado = float(input("Ingrese el lado de un cuadrado: "))
print("")
print("¿Que desea realiza?")
print("[1] Perimetro")
print("[2] Area")
##Seleccionamos si queremos que halle el perimetro o el area
opc = int(input("Respuesta: "));
print("")
##Se imprime la respuesta segun la opcion escogida
if opc == 1:
    print("El perimetro es ",perimetro(lado))
else:
    print("El area es ",area(lado))
print("")
