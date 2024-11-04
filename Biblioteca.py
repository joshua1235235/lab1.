import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime


conn = sqlite3.connect('actividad_fisica.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS ejercicios (
    id INTEGER PRIMARY KEY,
    fecha TEXT,
    tipo_actividad TEXT,
    duracion INTEGER,
    intensidad TEXT
)
''')
conn.commit()


def registrar_ejercicio():
    fecha = datetime.now().strftime("%Y-%m-%d")
    tipo_actividad = tipo_entry.get()
    duracion = duracion_entry.get()
    intensidad = intensidad_entry.get()
    
    if not tipo_actividad or not duracion or not intensidad:
        messagebox.showerror("Error", "Por favor, completa todos los campos")
        return
    
    try:
        duracion = int(duracion)
    except ValueError:
        messagebox.showerror("Error", "La duración debe ser un número entero")
        return
    
    c.execute('''
    INSERT INTO ejercicios (fecha, tipo_actividad, duracion, intensidad)
    VALUES (?, ?, ?, ?)
    ''', (fecha, tipo_actividad, duracion, intensidad))
    conn.commit()
    messagebox.showinfo("Éxito", "Ejercicio registrado correctamente")
    limpiar_campos()

def limpiar_campos():
    tipo_entry.delete(0, tk.END)
    duracion_entry.delete(0, tk.END)
    intensidad_entry.delete(0, tk.END)


def mostrar_progreso():
    c.execute('SELECT fecha, duracion FROM ejercicios')
    datos = c.fetchall()
    if not datos:
        messagebox.showinfo("Sin datos", "No hay registros de ejercicios para mostrar.")
        return
    
    df = pd.DataFrame(datos, columns=["Fecha", "Duración"])
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    df = df.groupby("Fecha").sum()  
    
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df["Duración"], marker='o', linestyle='-', color='b')
    plt.title("Progreso de Actividad Física")
    plt.xlabel("Fecha")
    plt.ylabel("Duración (minutos)")
    plt.grid()
    plt.show()


root = tk.Tk()
root.title("Seguimiento de Actividad Física")


tk.Label(root, text="Tipo de actividad:").grid(row=0, column=0)
tipo_entry = tk.Entry(root)
tipo_entry.grid(row=0, column=1)

tk.Label(root, text="Duración (min):").grid(row=1, column=0)
duracion_entry = tk.Entry(root)
duracion_entry.grid(row=1, column=1)

tk.Label(root, text="Intensidad (Baja, Media, Alta):").grid(row=2, column=0)
intensidad_entry = tk.Entry(root)
intensidad_entry.grid(row=2, column=1)

# Botones
registrar_button = tk.Button(root, text="Registrar Ejercicio", command=registrar_ejercicio)
registrar_button.grid(row=3, column=0, columnspan=2, pady=10)

progreso_button = tk.Button(root, text="Mostrar Progreso", command=mostrar_progreso)
progreso_button.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
