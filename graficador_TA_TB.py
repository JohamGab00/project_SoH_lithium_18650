import matplotlib.pyplot as plt
import sys
def main(parametro):
    # Definir listas para almacenar los datos de temperatura del ánodo y temperatura del cátodo
    temperatura_anodo_values = []  # Cambiar el nombre de la lista
    temperatura_catodo_values = []  # Cambiar el nombre de la lista
    tiempo_values = []  # Agregar una lista para almacenar el tiempo

    # Leer los datos del archivo
    with open(parametro, 'r') as file:
        tiempo = 0  # Inicializar el tiempo en 0 segundos
        for line in file:
            line = line.strip()
            if line.startswith("Temperatura A:"):
                temperatura_anodo_values.append(float(line.split(":")[1]))
                tiempo_values.append(tiempo)
            elif line.startswith("Temperatura B:"):
                temperatura_catodo_values.append(float(line.split(":")[1]))
            tiempo += 1.25  # Incrementar el tiempo en 2.5 segundos

    # Crear la gráfica superpuesta
    plt.figure(figsize=(12, 6))

    plt.plot(tiempo_values, temperatura_anodo_values, marker='o', linestyle='-', color='b', label='Temperatura del ánodo')  # Cambiar la etiqueta
    plt.plot(tiempo_values, temperatura_catodo_values, marker='o', linestyle='-', color='r', label='Temperatura del cátodo')  # Cambiar la etiqueta

    plt.ylabel('Temperatura (C)')
    plt.title('Gráfica de temperaturas en función del Tiempo')
    plt.xlabel('Tiempo (s)')
    plt.grid(True)
    plt.legend()  # Agregar una leyenda para identificar las dos curvas
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: graficador_TA_TB.py <parametro>")
    else:
        parametro = sys.argv[1]
        main(parametro)

