import tkinter as tk
from tkinter import messagebox, ttk

# Constantes de conversión y precio
CONVERSION_GALONES_A_LITROS = 3.78541
CONVERSION_LITROS_A_GALONES = 1 / 3.78541

# Función para la máquina de Turing de galones a litros
def maquina_turing_galones_a_litros(galones):
    cinta = list(str(galones))
    estado = 'inicio'
    cabezal = 0
    while estado != 'fin':
        if estado == 'inicio':
            if cinta[cabezal] == '.':
                estado = 'decimal'
                cabezal += 1
            else:
                cabezal += 1
        elif estado == 'decimal':
            if cabezal == len(cinta):
                estado = 'convertir'
            else:
                cabezal += 1
        elif estado == 'convertir':
            valor = float(''.join(cinta))
            litros = valor * CONVERSION_GALONES_A_LITROS
            return round(litros, 2)
    return 0

# Función para la máquina de Turing de litros a galones
def maquina_turing_litros_a_galones(litros):
    cinta = list(str(litros))
    estado = 'inicio'
    cabezal = 0
    while estado != 'fin':
        if estado == 'inicio':
            if cinta[cabezal] == '.':
                estado = 'decimal'
                cabezal += 1
            else:
                cabezal += 1
        elif estado == 'decimal':
            if cabezal == len(cinta):
                estado = 'convertir'
            else:
                cabezal += 1
        elif estado == 'convertir':
            valor = float(''.join(cinta))
            galones = valor * CONVERSION_LITROS_A_GALONES
            return round(galones, 2)
    return 0

# Función de transformación
def transformar():
    if(entry_venta_litro.get() == ""):
        messagebox.showerror("Error", "Por favor ingrese un precio de venta de litros.")
        return
    elif(not entry_venta_litro.get().isdigit()):
        messagebox.showerror("Error", "Por favor ingrese digitos.")
        return
    if(entry_gasto_galones.get() == ""):
        messagebox.showerror("Error", "Por favor ingrese el gasto por los galones.")
        return
    elif(not entry_gasto_galones.get().isdigit()):
        messagebox.showerror("Error", "Por favor ingrese digitos.")
        return
    cadena = entry_cadena_galones.get()
    precio_por_litro = float(entry_venta_litro.get().replace("$", ""))
    gasto_galones = float(entry_gasto_galones.get().replace("$", ""))
    try:
        if "gal" in cadena:
            galones = float(cadena.replace("gal", ""))
            litros = maquina_turing_galones_a_litros(galones)
            entry_read_transform.config(state='normal')
            entry_read_transform.delete(0, tk.END)
            entry_read_transform.insert(0, f"{litros} L")
            entry_read_transform.config(state='readonly')
                        
            ganancia_bruta = litros * precio_por_litro
            entry_ganancia_bruta.config(state='normal')
            entry_ganancia_bruta.delete(0, tk.END)
            entry_ganancia_bruta.insert(0, f"${ganancia_bruta:.2f}")
            entry_ganancia_bruta.config(state='readonly')

            ganancia_neta = ganancia_bruta - gasto_galones
            entry_ganancia_neta.config(state='normal')
            entry_ganancia_neta.delete(0, tk.END)
            entry_ganancia_neta.insert(0, f"${ganancia_neta:.2f}")
            entry_ganancia_neta.config(state='readonly')
            
            
        elif "L" in cadena:
            litros = float(cadena.replace("L", ""))
            galones = maquina_turing_litros_a_galones(litros)
            entry_read_transform.config(state='normal')
            entry_read_transform.delete(0, tk.END)
            entry_read_transform.insert(0, f"{galones} gal")
            entry_read_transform.config(state='readonly')
                        
            ganancia_bruta = litros * precio_por_litro
            entry_ganancia_bruta.config(state='normal')
            entry_ganancia_bruta.delete(0, tk.END)
            entry_ganancia_bruta.insert(0, f"${ganancia_bruta:.2f}")
            entry_ganancia_bruta.config(state='readonly')

            ganancia_neta = ganancia_bruta - gasto_galones
            entry_ganancia_neta.config(state='normal')
            entry_ganancia_neta.delete(0, tk.END)
            entry_ganancia_neta.insert(0, f"${ganancia_neta:.2f}")
            entry_ganancia_neta.config(state='readonly')
            
        else:
            messagebox.showerror("Error", "Cadena no válida. Debe incluir 'gal' o 'L'.")
    
    except ValueError:
        messagebox.showerror("Error", "Entrada no válida. Por favor, ingrese un número válido.")


root = tk.Tk()
root.title("Conversor de Galones a Litros")
root.geometry("500x175")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

ttk.Label(root, text="Ingreso").grid(column=0, row=0)

ttk.Label(root, text="Gasto invertido:").grid(column=0, row=1)
entry_gasto_galones = ttk.Entry(root)
entry_gasto_galones.grid(column=0, row=2)

ttk.Label(root, text="Venta por litro:").grid(column=0, row=3)
entry_venta_litro = ttk.Entry(root)
entry_venta_litro.grid(column=0, row=4)

ttk.Label(root, text="Cadena de galones o litros").grid(column=1, row=0)

entry_cadena_galones = ttk.Entry(root, width=30)
entry_cadena_galones.grid(column=1, row=1, rowspan=3)

entry_read_transform = ttk.Entry(root, state='readonly')
entry_read_transform.grid(column=1, row=4)

boton_transformar = ttk.Button(root, text="Transformar", command=transformar)
boton_transformar.grid(column=1, row=5)

ttk.Label(root, text="Salida").grid(column=2, row=0)

ttk.Label(root, text="Ganancia bruta:").grid(column=2, row=1)
entry_ganancia_bruta = ttk.Entry(root, state='readonly')
entry_ganancia_bruta.grid(column=2, row=2)

ttk.Label(root, text="Ganancia neta:").grid(column=2, row=3)
entry_ganancia_neta = ttk.Entry(root, state='readonly')
entry_ganancia_neta.grid(column=2, row=4)


root.mainloop()
