n = int(input("Ingresa hasta que posicion quieres encontrar la secuencia de lucas: "))

if n == 1:
    print("2")
elif n == 2:
    print("1")
Lucas = [2,1]

while len(Lucas) < n:
    suma = Lucas[-1] + Lucas[-2]
    Lucas.append(suma)
    print(Lucas)
print(f"El numero de la posicion {n} de la Sucesion de Lucas es: {Lucas[-1]}")