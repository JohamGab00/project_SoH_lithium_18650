import tkinter as tk
from tkinter import messagebox
import subprocess

# Funciones para ejecutar los scripts con parámetros
def ejecutar_script(script, parametros):
    try:
        resultado = subprocess.run(["python", script] + parametros, capture_output=True, text=True, check=True)
        messagebox.showinfo("Resultado", resultado.stdout)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error al ejecutar el script: {e.stderr}")

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Menú de Scripts")
ventana.geometry("400x300")

# Etiquetas y campos de entrada
etiqueta_parametro = tk.Label(ventana, text="Parámetro:")
etiqueta_parametro.pack()
parametro_entry = tk.Entry(ventana)
parametro_entry.pack()

etiqueta_voltaje_nominal = tk.Label(ventana, text="Voltaje Nominal (V):")
etiqueta_voltaje_nominal.pack()
voltaje_nominal_entry = tk.Entry(ventana)
voltaje_nominal_entry.pack()

etiqueta_tension_de_corte = tk.Label(ventana, text="Tensión de Corte (V):")
etiqueta_tension_de_corte.pack()
tension_de_corte_entry = tk.Entry(ventana)
tension_de_corte_entry.pack()

# Botones para ejecutar scripts con parámetros
boton_script1 = tk.Button(ventana, text="Graficar datos de Corriente y Voltaje", command=lambda: ejecutar_script("graficador_V_I.py", [parametro_entry.get()]))
boton_script2 = tk.Button(ventana, text="Graficar datos de Temperatura", command=lambda: ejecutar_script("graficador_TA_TB.py", [parametro_entry.get()]))
boton_script3 = tk.Button(ventana, text="Solicitar estado de salud (SOH)", command=lambda: ejecutar_script("capacidad_real.py", [parametro_entry.get(), voltaje_nominal_entry.get(), tension_de_corte_entry.get()]))

boton_script1.pack()
boton_script2.pack()
boton_script3.pack()

# Ejecutar la aplicación
ventana.mainloop()
