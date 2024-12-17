import random

def llegir_llista_enters():
    llista = []
    entrada = ""
    while entrada != ".":
        entrada = input("Introduce un numero: ")
        if entrada == ".":
            break
        llista.append(int(entrada))

def senars_llista(llista):
    impares = []
    for e in llista:
        if e % 2 != 0:
            impares.append(e)
    print(impares)

def sumar_parells_llista(llista):
    suma = 0
    for e in llista:
        if e % 2 == 0:
            suma += e
    print(suma)
    
def cercar_numero_llista(llista, numero):
    numero = input("Que numero quieres buscar: ")
    encontrado = False
    for e in enumerate(llista):
        if numero == e[1]:
            encontrado = True
            print(e[0]+1)
    if not encontrado:
        print("-1")

def llegir_llista_paraules():
    llista = []
    entrada = ""
    while entrada != ".":
        entrada = input("Introduce una palabra: ")
        if entrada == ".":
            break
        llista.append(str(entrada))

def crear_paraula_llista(llista):
    iniciales = ""
    for e in llista:
        iniciales += e[0]
    print(iniciales)
    
def crear_llista_num_aleatoris():
    aleatorios = []
    for e in range(5):
        aleatorios.append(random.randint(1, 100))
    print(aleatorios)

def comparar_llistes(llista1, llista2):
    comparador = []
    for e1, e2 in zip(llista1, llista2):
            if e2 == e1:
                comparador.append(2)
            elif e2 in llista1:
                comparador.append(1)
            else:
                comparador.append(0)
    print(comparador)

def majors_edat(edat1, edat2):
    if edat1 >= 18:
        print("La edad '{}' es mayor de edad".format(edat1))
    else:
        print("La edad '{}' es menor de edad".format(edat1))
    if edat2 >= 18:
        print("La edad '{}' es mayor de edad".format(edat2))
    else:
        print("La edad '{}' es menor de edad".format(edat2))
        
def menu():
    print("""MENU:
1. Lista enteros
2. Lista impares
3. Sumar lista pares
4. Buscar numero lista
5. Leer lista palabras
6. Crear lista palabras
7. Lista numeros aleatorios
8. Comparar listas
9. Mayores de edad
10. Salir          
          """)
    menuelegir = input("Elige con un numero: ")
    match menuelegir:
        case "1":
            llegir_llista_enters()
        case "2":
            senars_llista(llista = [1, 2, 3, 4, 5])
        case "3":
            sumar_parells_llista(llista = [1, 2, 3, 4, 5])
        case "4":
            cercar_numero_llista(llista = [1, 2, 3, 4, 5], numero = 2)
        case "5":
            llegir_llista_paraules()
        case "6":
            crear_paraula_llista(llista = ["Hola", "que", "tal"])
        case "7":
            crear_llista_num_aleatoris()
        case "8":
            comparar_llistes(llista1 = [1, 2, 3, 4, 5], llista2 = [1, 6, 2, 8, 9])
        case "9":
            majors_edat(edat1 = 18, edat2 = 17)
        case "10":
            exit()
    
# PROGRAMA

while True:
    menu()