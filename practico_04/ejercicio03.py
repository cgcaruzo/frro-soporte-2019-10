## 3 Ejercicio Crear un Formulario que usando el control Treeview muestre la una lista con los nombre de
## Ciudades Argentinas y su código postal ( por lo menos 5 ciudades ) .

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Ciudades")
root.resizable(False, False)

tree=ttk.Treeview(root)
tree["columns"]=("cod_postal")
tree.column("#0", width=270, minwidth=270, stretch=tk.NO)
tree.column("cod_postal", width=150, minwidth=150, stretch=tk.NO)

tree.heading("#0",text="Ciudad",anchor=tk.W)
tree.heading("cod_postal", text="Cod. Postal",anchor=tk.W)

tree.insert("", tk.END, text="Venado Tuerto", values="2600")
tree.insert("", tk.END, text="Rosario", values="2000")
tree.insert("", tk.END, text="La Plata", values="1900")
tree.insert("", tk.END, text="Villa Cañas", values="2607")
tree.insert("", tk.END, text="Capitán Bermudez", values="2154")
tree.insert("", tk.END, text="Santa Fe", values="3000")


tree.pack(side=tk.TOP,fill=tk.X)



root.mainloop()
