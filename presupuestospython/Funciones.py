class Presupuesto:
    def __init__(self):
        # Definición de atributos de la clase
        self.meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre",
                      "Octubre", "Noviembre", "Diciembre"]
        self.ingresos_por_fuente = {}
        self.gastos = {}
        self.gastos_operativos = {}
        self.flujo_caja = {}
        self.balance_cuentas = {}
        self.deudas = {}
        self.costos_fijos = {}
        self.costos_variables = {}
        self.costos_de_ventas = {}
        self.costos_financieros = {}
        self.inversiones_financieras = {}
        self.inversiones_capital = {}
        self.reservas_provisiones = {}
        self.inversiones = {}
        self.lista_inversiones = []
        self.depreciacion = {}
        self.amortizacion = {}
        self.impuestos = {}
        self.margen_beneficio = {}
        self.roi = {}
        self.ebitda = {}
        self.capital_trabajo = {}
        self.reserva_efectivo = {}
        self.proyeccion_venta = {}
        self.costos_operacion = {}
        self.costos_produccion = {}
        self.salarios = {}
        self.alquiler_lugar = {}
        self.servicios_publicos = {}
        self.inversion_planificada = {}
        self.proveedores = {}
        self.precio_venta = {}
    
    def solicitar_reserva_efectivo(self):
        for mes in self.meses:
            while True:
                try:
                    self.reserva_efectivo[mes] = float(input(f"Ingrese el monto de sus reservas de efectivo para {mes}: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un valor numérico.")

    def solicitar_ingresos_por_fuente(self): 
        for mes in self.meses:
            ingresos_por_fuente_mes = {}
            for fuente in ["Ventas", "Prestaciones dadas", "Alquiler/es", "Otros"]:
                while True:
                    try:
                        ingreso = float(input(f"Ingrese los ingresos para {fuente} en {mes}: (0 si no aplica) "))
                        break
                    except ValueError:
                        print("Por favor, ingrese un valor numérico.")
                ingresos_por_fuente_mes[fuente] = ingreso
            self.ingresos_por_fuente[mes] = ingresos_por_fuente_mes
    
    def solicitar_gastos_operativos(self):  
        for mes in self.meses:
            gastos_operativos_mes = {}
            for categoria in ["Marketing","Proveedores", "Investigación y Desarrollo", "Servicios Profesionales",
                              "Salarios","Impuestos","Costos operativos","Alquiler", "Otros"]: 
                while True:
                    try:
                        gasto_operativo = float(input(f"Ingrese los gastos para {categoria} en {mes}: (0 si no aplica) "))
                        break
                    except ValueError:
                        print("Por favor, ingrese un valor numérico.")
                gastos_operativos_mes[categoria] = gasto_operativo
            self.gastos_operativos[mes] = gastos_operativos_mes 

    def solicitar_deudas(self):
        for mes in self.meses: 
            while True:
                try:
                    self.deudas[mes] = float(input(f"Ingrese el monto actual de su deuda en {mes} (o 0 si no tiene deudas): "))
                    break
                except ValueError:
                    print("Por favor, ingrese un valor numérico.")
   
    def solicitar_costos_fijos(self):
        for mes in self.meses:
            while True:
                try:
                    self.costos_fijos[mes] = float(input(f"Ingrese los costos fijos totales para {mes}: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un valor numérico.")
    
    def solicitar_costos_variables(self): 
        for mes in self.meses:
            while True:
                try:
                    self.costos_variables[mes] = float(input(f"Ingrese el monto de los costos variables actuales para {mes}: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un valor numérico.")

    def solicitar_flujo_caja(self):
        for mes in self.meses:
            while True:
                try:
                    self.flujo_caja[mes] = float(input(f"Ingrese el monto del flujo de caja para {mes}: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un valor numérico.")
    
    def solicitar_balance_cuentas(self):
        for mes in self.meses:
            while True:
                try:
                    self.balance_cuentas[mes] = float(input(f"Ingrese el monto actual del balance de cuentas para {mes}: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un valor numérico.")
   
    def solicitar_inversiones(self):
        for mes in self.meses:
            while True:
                try:
                    self.inversiones[mes] = float(input(f"Ingrese el monto invertido para {mes} (o 0 si no ha invertido): "))
                    break
                except ValueError:
                    print("Por favor, ingrese un valor numérico.")

    def solicitar_inversiones_planificadas(self):
        for mes in self.meses:
            while True:
                try:
                    self.inversion_planificada[mes] = float(input(f"Ingrese el monto que pretende invertir en {mes}: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un valor numérico.")

    def solicitar_margen_beneficio(self):
        for mes in self.meses:
            while True:
                try:
                    self.margen_beneficio[mes] = float(input(f"Ingrese el monto total del margen de beneficios obtenido para {mes}: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un valor numérico.")

    def solicitar_depreciacion_amortizacion(self):
        for mes in self.meses:
            while True:
                try:
                    self.depreciacion[mes] = float(input(f"Ingrese el monto de depreciación para {mes}: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un valor numérico.")

            while True:
                try:
                    self.amortizacion[mes] = float(input(f"Ingrese el monto de amortización para {mes}: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un valor numérico.")

    def solicitar_roi(self):
        for mes in self.meses:
            while True:
                try:
                    self.roi[mes] = float(input(f"Ingrese el monto retornado de sus inversiones para {mes}: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un valor numérico.")

    def solicitar_ebitda(self):
        for mes in self.meses:
            while True:
                try:
                    self.ebitda[mes] = float(input(f"Ingrese el monto total de ingresos sin deducir impuestos, intereses, depreciación y amortización para {mes}: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un valor numérico.")

    def solicitar_capital_trabajo(self):
        for mes in self.meses:
            while True:
                try:
                    self.capital_trabajo[mes] = float(input(f"Ingrese el monto retenido para corto plazo para {mes}: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un valor numérico.")

    def solicitar_proyeccion_ventas(self):
        for mes in self.meses:
            while True:
                try:
                    self.proyeccion_venta[mes] = float(input(f"Ingrese su proyección de venta para {mes}: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un valor numérico.")

    def totalizar_ingresos(self):
        total_ingresos = sum(sum(mes.values()) for mes in self.ingresos_por_fuente.values())
        return total_ingresos

    def totalizar_gastos(self):
        total_gastos = sum(self.gastos.values()) + sum(self.salarios.values()) + \
                       sum(sum(mes.values()) for mes in self.gastos_operativos.values()) + \
                       sum(self.costos_fijos.values()) + sum(self.costos_variables.values()) + \
                       sum(self.impuestos.values())
        return total_gastos

    def calcular_ganancias_perdidas(self):
        total_ingresos = self.totalizar_ingresos()
        total_gastos = self.totalizar_gastos()
        ganancias_perdidas = total_ingresos - total_gastos
        return ganancias_perdidas

    def calcular_margen_beneficio_anual(self):
        ganancias_perdidas = self.calcular_ganancias_perdidas()
        total_ingresos = self.totalizar_ingresos()
        margen_beneficio_anual = (ganancias_perdidas / total_ingresos) * 100
        return margen_beneficio_anual

    def calcular_flujo_efectivo_neto_anual(self):
        total_ingresos = self.totalizar_ingresos()
        total_gastos = self.totalizar_gastos()
        flujo_efectivo_neto_anual = total_ingresos - total_gastos
        return flujo_efectivo_neto_anual

    def calcular_presupuesto(self):
        for mes in self.meses:
            print(f'\nPresupuesto para {mes}:')

            # Cálculo de los ingresos por fuente
            ingresos_por_fuente_mes = self.ingresos_por_fuente.get(mes, {})
            ingresos_por_fuente_mes_total = sum(ingresos_por_fuente_mes.values())
            if ingresos_por_fuente_mes_total:
                print("Ingresos por Fuente:")
                for fuente, ingreso in ingresos_por_fuente_mes.items():
                    print(f"{fuente}: {ingreso}")
                ingresos = ingresos_por_fuente_mes_total  

            # Cálculo de los gastos operativos
            gastos = 0
            gastos_operativos_mes = self.gastos_operativos.get(mes, {})
            gastos_operativos_total = sum(gastos_operativos_mes.values())
            if gastos_operativos_total:
                print("Gastos Operativos:")
                for categoria, gasto in gastos_operativos_mes.items():
                    print(f"{categoria}: {gasto}")
                gastos += gastos_operativos_total

            # Cálculo de los costos totales
            costos = self.costos_fijos.get(mes, 0) + self.costos_variables.get(mes, 0)

            # Cálculo de la depreciación y amortización
            depreciacion_amortizacion = self.depreciacion.get(mes, 0) + self.amortizacion.get(mes, 0)

            # Cálculo de los impuestos
            impuestos = self.impuestos.get(mes, 0)
            
            #Obtenemos ROI
            roi = self.roi.get(mes, 0)

            # Cálculo del margen de beneficio y EBITDA
            margen_beneficio = ingresos - (gastos + costos)
            ebitda = ingresos - (gastos + costos + depreciacion_amortizacion + impuestos)

            print(f'Ingresos: {ingresos}')
            print(f'Gastos: {gastos}')
            print(f'Costos: {costos}')
            print(f'Depreciación y Amortización: {depreciacion_amortizacion}')
            print(f'Impuestos: {impuestos}')
            print(f'Margen de Beneficio: {margen_beneficio}')
            print(f'ROI: {roi}')
            print(f'EBITDA: {ebitda}')
    
    def calcular_presupuesto_final(self, tasa_descuento):
        fcd_total = 0
        
        for i, mes in enumerate(self.meses):
            if mes in self.flujo_caja:
                fcd_total += self.flujo_caja[mes] / ((1 + tasa_descuento) ** (i + 1))
        
        vpn = fcd_total - sum(self.inversiones.values())
        
        
        print(f'Flujo de Caja Descontado (FCD) Total: {fcd_total}')
        print(f'Valor Presente Neto (VPN): {vpn}')