import sys

def main(parametro, voltaje_nominal, tension_de_corte):
    # Definir una lista para almacenar los datos de corriente
    corriente_values = []
    voltaje_values = []

    # Leer los datos del archivo
    with open(parametro, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("Corriente:"):
                corriente_values.append(float(line.split(":")[1]))

    # Calcular el valor promedio del voltaje
    if voltaje_values:
        average_voltaje = sum(voltaje_values) / len(voltaje_values)

    # Calcular el valor promedio de la corriente
    if corriente_values:
        average_current = sum(corriente_values) / len(corriente_values)

        # Calcular el tiempo transcurrido en horas
        tiempo_transcurrido_segundos = len(corriente_values) * 5  # 5 segundos por medición
        tiempo_transcurrido_horas = tiempo_transcurrido_segundos / 3600  # 3600 segundos en una hora

        #para imprimir horas y minutos

        tiempo_horas = tiempo_transcurrido_segundos // 3600  # Parte entera de las horas
        tiempo_minutos = (tiempo_transcurrido_segundos % 3600) // 60  # Parte entera de los minutos


        # Obtener voltaje nominal y tensión de corte de los argumentos
        voltaje_nominal = float(voltaje_nominal)
        tension_de_corte = float(tension_de_corte)
        
        # Calcular la capacidad real de la celda en miliamperios-hora (mAh)
        capacidad_real_mah = (average_current * tiempo_transcurrido_horas * 1000) / (voltaje_nominal - tension_de_corte)


        
        # Calcular estado de salud de la celda
        salud = (capacidad_real_mah * 100) / (2500)
        print(f"Corriente promedio: {average_current} A")
        print(f"Tiempo transcurrido: {tiempo_horas} horas {tiempo_minutos} minutos")
        print(f"Voltaje nominal: {voltaje_nominal} V")
        print(f"Tensión de corte: {tension_de_corte} V")
        print(f"Capacidad real de la celda: {capacidad_real_mah} mAh")
        print(f"Estado de salud de la celda: {salud} % de vida útil")
    else:
        print("No se encontraron datos de corriente en el archivo")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: capacidad_real.py <parametro> <voltaje_nominal> <tension_de_corte>")
    else:
        parametro = sys.argv[1]
        voltaje_nominal = sys.argv[2]
        tension_de_corte = sys.argv[3]
        main(parametro, voltaje_nominal, tension_de_corte)
