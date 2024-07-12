import random
import csv
import math

trabajadores = [
    {"nombre": "Juan Perez", "cargo": "Consultor TI"},
    {"nombre": "Maria Garcia", "cargo": "Analista"},
    {"nombre": "Carlos Lopez", "cargo": "Programador"},
    {"nombre": "Ana Martinez", "cargo": "Jefe de Proyecto"},
    {"nombre": "Pedro Rodriguez", "cargo": "Consultor TI"},
    {"nombre": "Laura Hernandez", "cargo": "Analista"},
    {"nombre": "Miguel Sanchez", "cargo": "Programador"},
    {"nombre": "Isabel Gomez", "cargo": "Jefe de Proyecto"},
    {"nombre": "Francisco Diaz", "cargo": "Consultor TI"},
    {"nombre": "Elena Fernandez", "cargo": "Analista"}
]

def asignar_sueldos():
    return [random.randint(300000, 2500000) for _ in trabajadores]

def imprimir_clasificacion(sueldos, rango, mensaje):
    print(f"\n{mensaje} TOTAL:", len(rango))
    for i in rango:
        trabajador = trabajadores[i]
        sueldo = sueldos[i]
        print(f"Nombre empleado: {trabajador['nombre']} Sueldo: ${sueldo}")

def clasificar_sueldos(sueldos):
    menores_800k = [i for i, s in enumerate(sueldos) if s < 800000]
    entre_800k_2000k = [i for i, s in enumerate(sueldos) if 800000 <= s <= 2000000]
    mayores_2000k = [i for i, s in enumerate(sueldos) if s > 2000000]

    imprimir_clasificacion(sueldos, menores_800k, "Sueldos menores a $800.000")
    imprimir_clasificacion(sueldos, entre_800k_2000k, "Sueldos entre $800.000 y $2.000.000")
    imprimir_clasificacion(sueldos, mayores_2000k, "Sueldos superiores a $2.000.000")

    print("\nTOTAL SUELDOS:", sum(sueldos))

def ver_estadisticas(sueldos):
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    sueldo_promedio = sum(sueldos) / len(sueldos)
    sueldo_geom = math.exp(sum(math.log(s) for s in sueldos) / len(sueldos))

    print(f"\nSueldo mas alto: ${sueldo_max}")
    print(f"Sueldo mas bajo: ${sueldo_min}")
    print(f"Promedio de sueldos: ${sueldo_promedio:.2f}")
    print(f"Media geometrica de sueldos: ${sueldo_geom:.2f}")

def generar_reporte(sueldos):
    with open('reporte_sueldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Cargo", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Liquido"])

        for trabajador, sueldo in zip(trabajadores, sueldos):
            descuento_salud = sueldo * 0.07
            descuento_afp = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            writer.writerow([trabajador["nombre"], trabajador["cargo"], sueldo, descuento_salud, descuento_afp, sueldo_liquido])
            print(f"\nNombre empleado: {trabajador['nombre']} Cargo: {trabajador['cargo']} Sueldo Base: ${sueldo} Descuento Salud: ${descuento_salud:.2f} Descuento AFP: ${descuento_afp:.2f} Sueldo Liquido: ${sueldo_liquido:.2f}")

def salir_programa():
    print("Finalizando programa...")
    print("Desarrollado por: Matias Cuevas")
    print("RUT: 21.756.487-1")

def menu():
    sueldos = []
    while True:
        print("\nMenu:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadisticas")
        print("4. Generar reporte de sueldos")
        print("5. Salir del programa")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            sueldos = asignar_sueldos()
            print("\nSueldos asignados aleatoriamente.")
        elif opcion == "2":
            if sueldos:
                clasificar_sueldos(sueldos)
            else:
                print("Primero asigne sueldos.")
        elif opcion == "3":
            if sueldos:
                ver_estadisticas(sueldos)
            else:
                print("Primero asigne sueldos.")
        elif opcion == "4":
            if sueldos:
                generar_reporte(sueldos)
            else:
                print("Primero asigne sueldos.")
        elif opcion == "5":
            salir_programa()
            break
        else:
            print("Opcion no valida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
