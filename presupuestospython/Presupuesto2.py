from Funciones import *

# Uso del programa
presupuesto = Presupuesto()


def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Ingresar ingresos por fuente")
    print("2. Ingresar gastos actuales")
    print("3. Ingresar gastos operativos")
    print("4. Ingresar inversiones")
    print("5. Ingresar costos fijos")
    print("6. Ingresar ROI")
    print("7. Ingresar depreciación y amortización")
    print("8. Calcular presupuesto")
    print("9. Calcular presupuesto final")
    print("10. Salir") 


while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        presupuesto.solicitar_ingresos_por_fuente()   
    elif opcion == "2":
        presupuesto.solicitar_gastos_operativos()
    elif opcion == "3":
        presupuesto.solicitar_inversiones()
    elif opcion == "4":
        presupuesto.solicitar_costos_fijos()
    elif opcion == "5":
        presupuesto.solicitar_roi()
    elif opcion == "6":
        presupuesto.solicitar_depreciacion_amortizacion()
    elif opcion == "7":
        presupuesto.calcular_presupuesto()
    elif opcion == "8":
        tasa_descuento = 0.1  # Puedes cambiar la tasa de descuento según tu necesidad
        presupuesto.calcular_presupuesto_final(tasa_descuento)
    elif opcion == "9":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")