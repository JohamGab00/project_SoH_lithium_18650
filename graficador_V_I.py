import matplotlib.pyplot as plt
import sys
def main(parametro):
    # Definir listas para almacenar los datos de corriente y voltaje
    corriente_values = []
    voltaje_values = []
    tiempo_values = []  # Agregar una lista para almacenar el tiempo

    # Leer los datos del archivo
    with open(parametro, 'r') as file:
        leyendo_corriente = True
        tiempo = 0  # Inicializar el tiempo en 0 segundos
        for line in file:
            line = line.strip()
            if line.startswith("Corriente:"):
                corriente_values.append(float(line.split(":")[1]))
                voltaje_values.append(None)  # Agregar un marcador None para el voltaje
                tiempo_values.append(tiempo)
                leyendo_corriente = True
            elif line.startswith("Voltaje:"):
                voltaje_values.append(float(line.split(":")[1]))
                corriente_values.append(None)  # Agregar un marcador None para la corriente
                tiempo_values.append(tiempo)
                leyendo_corriente = False
            tiempo += 1.25  # Incrementar el tiempo en 5 segundo

    # Crear las gráficas
    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)  # Dos filas, una columna, primera gráfica
    plt.plot(tiempo_values, corriente_values, marker='o', linestyle='-', color='b')
    plt.ylabel('Corriente (A)')
    plt.title('Gráfica de Corriente en función del Tiempo')

    plt.subplot(2, 1, 2)  # Dos filas, una columna, segunda gráfica
    plt.plot(tiempo_values, voltaje_values, marker='o', linestyle='-', color='r')
    plt.ylabel('Voltaje (V)')
    plt.title('Gráfica de Voltaje en función del Tiempo')

    plt.xlabel('Tiempo (s)')
    plt.tight_layout()  # Ajustar automáticamente la disposición de las gráficas
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: graficador_V_I.py <parametro>")
    else:
        parametro = sys.argv[1]
        main(parametro)



