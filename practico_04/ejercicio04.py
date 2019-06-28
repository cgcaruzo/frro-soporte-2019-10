## 4. Ejercicio al Formulario del Ejercicio 3 ,  agrege  los siguientes botones 1- un  botón  Alta 
## que inicia otra venta donde puedo ingresar una ciudad y su código postal .
## 2 – un botón Baja que borra del listad de ciudades la ciudad que esta selecionada en Treeview .
## 3 – un botón Modificar . Todos los cambios se deben ver reflejados en la lista que se muestra . 


from tkinter import *
from tkinter import ttk

class Aplicacion():
    def __init__(self):
        self.root = Tk()
        self.root.title("Ciudades")
        self.root.resizable(False, False)
        self.createTreeview()
        self.botones()
        self.root.mainloop()
    
    def createTreeview(self):
        self.tree=ttk.Treeview(self.root)
        self.tree["columns"]=("cod_postal")
        self.tree.column("#0", width=270, minwidth=270, stretch=NO)
        self.tree.column("cod_postal", width=150, minwidth=150, stretch=NO)
    
        self.tree.heading("#0",text="Ciudad",anchor=W)
        self.tree.heading("cod_postal", text="Cod. Postal",anchor=W)
        self.tree.pack(side=TOP,fill=X)
    
        self.tree.insert("", END, text="Venado Tuerto", values="2600")
        self.tree.insert("", END, text="Rosario", values="2000")
        self.tree.insert("", END, text="La Plata", values="1900")
        self.tree.insert("", END, text="Villa Cañas", values="2607")
        self.tree.insert("", END, text="Capitán Bermudez", values="2154")
        self.tree.insert("", END, text="Santa Fe", values="3000")   
    
    def botones(self):
        btnAlta = Button(self.root, text="Alta", command=lambda: self.alta(), height=1, width=8,).pack(side=LEFT)
        btnBaja = Button(self.root, text="Baja", command=lambda: self.baja(), height=1, width=8,).pack(side=LEFT)
        btnModificar = Button(self.root, text="Modificar", command=lambda: self.modificar(), height=1, width=8,).pack(side=LEFT)
    
    def alta(self):
        alta = Toplevel(self.root)
        alta.title("Nueva ciudad")
    
        lblCiudad = Label(alta, text="Ciudad")
        vCiudad = StringVar()
        entCiudad = Entry(alta, textvariable=vCiudad)
        lblCodPostal = Label(alta, text="Cod. Postal")
        vCodpostal = StringVar()
        entCodPostal = Entry(alta, textvariable=vCodpostal)
        btnGuardar = Button(alta, text="Guardar", command=lambda: guardar(vCiudad.get(), vCodpostal.get()), height=1, width=8)
        btnCancelar = Button(alta, text="Cancelar", command=lambda: alta.destroy(), height=1, width=8)
    
        lblCiudad.grid(column=1, row=1, sticky='e'+'w')
        entCiudad.grid(column=2, row=1, sticky='e'+'w', columnspan=2)
        lblCodPostal.grid(column=1, row=2, sticky='e'+'w')
        entCodPostal.grid(column=2, row=2, sticky='e'+'w', columnspan=2)
    
        btnGuardar.grid(column=2, row=3, sticky='e'+'w')
        btnCancelar.grid(column=3, row=3, sticky='e'+'w')
    
        alta.grab_set()

        def guardar(ciudad, cod_postal):
            self.tree.insert("", END, text=ciudad, values=cod_postal)
            alta.destroy()

    def baja(self):
        self.tree.delete(self.tree.focus())
    
    def modificar(self):
        item = self.tree.selection()
        editar = Toplevel(self.root)
        editar.title("Editar ciudad")

        lblCiudad = Label(editar, text="Ciudad")
        vCiudad = StringVar()
        entCiudad = Entry(editar, textvariable=vCiudad)
        lblCodPostal = Label(editar, text="Cod. Postal")
        vCodpostal = StringVar()
        entCodPostal = Entry(editar, textvariable=vCodpostal)
        vCiudad.set(self.tree.item(self.tree.focus())['text'])
        vCodpostal.set(self.tree.item(self.tree.focus())['values'][0])

        btnGuardar = Button(editar, text="Guardar", command=lambda: guardar(item, vCiudad.get(), vCodpostal.get()), height=1, width=8)
        btnCancelar = Button(editar, text="Cancelar", command=lambda: editar.destroy(), height=1, width=8)

        lblCiudad.grid(column=1, row=1, sticky='e'+'w')
        entCiudad.grid(column=2, row=1, sticky='e'+'w', columnspan=2)
        lblCodPostal.grid(column=1, row=2, sticky='e'+'w')
        entCodPostal.grid(column=2, row=2, sticky='e'+'w', columnspan=2)

        btnGuardar.grid(column=2, row=3, sticky='e'+'w')
        btnCancelar.grid(column=3, row=3, sticky='e'+'w')

        editar.grab_set()

        def guardar(item, ciudad, cod_postal):
            self.tree.item(item, text=ciudad, values=cod_postal)
            editar.destroy()
    
if __name__ == "__main__":
    Aplicacion()
