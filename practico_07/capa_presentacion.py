from frro.practico05.ejercicio01 import Socio
from frro.practico_06.capa_negocio import NegocioSocio

from tkinter import *
from tkinter import ttk

class Presentacion():
    def __init__(self):
        self.root = Tk()
        self.root.title("ABM Socios")
        self.root.resizable(False, False)
        self.createTreeview()
        self.botones()
        self.root.mainloop()

    def createTreeview(self):
        self.negocio = NegocioSocio()
        socios = self.negocio.todos()

        self.tree=ttk.Treeview(self.root)
        self.tree["columns"]=("nombre", "apellido", "dni")
        self.tree.column("#0", width=150, minwidth=150, stretch=NO)
        self.tree.column("nombre", width=150, minwidth=150, stretch=NO)
        self.tree.column("apellido", width=150, minwidth=150, stretch=NO)
        self.tree.column("dni", width=150, minwidth=150, stretch=NO)

        self.tree.heading("#0",text="Id", anchor=W)
        self.tree.heading("nombre", text="Nombre", anchor=W)
        self.tree.heading("apellido", text="Apellido", anchor=W)
        self.tree.heading("dni", text="DNI", anchor=W)
        self.tree.pack(side=TOP,fill=X)

        for i in socios:
            self.tree.insert("", END, text=str(i.id), values=(i.nombre, i.apellido, i.dni), iid=i.id)

    def botones(self):
        bAlta = Button(self.root, text="Alta", command=lambda: self.alta(), height=1, width=8,).pack(side=LEFT)
        bBaja = Button(self.root, text="Baja", command=lambda: self.baja(), height=1, width=8,).pack(side=LEFT)
        bModificar = Button(self.root, text="Modificar", command=lambda: self.modificar(), height=1, width=8,).pack(side=LEFT)

    def alta(self):
        alta = Toplevel(self.root)
        alta.title("Nuevo socio")

        lNombre = Label(alta, text="Nombre")
        vNombre = StringVar()
        anombre = Entry(alta, textvariable=vNombre)
        lApellido = Label(alta, text="Apellido")
        vApellido = StringVar()
        aapellido = Entry(alta, textvariable=vApellido)
        lDni = Label(alta, text="Dni")
        vDni= StringVar()
        adni = Entry(alta, textvariable=vDni)
        bGuardar = Button(alta, text="Guardar", command=lambda: guardar(vNombre.get(), vApellido.get(), vDni.get()), height=1, width=8)
        bCancelar = Button(alta, text="Cancelar", command=lambda: alta.destroy(), height=1, width=8)

        lNombre.grid(column=1, row=1, sticky='e'+'w')
        anombre.grid(column=2, row=1, sticky='e'+'w', columnspan=2)
        lApellido.grid(column=1, row=2, sticky='e'+'w')
        aapellido.grid(column=2, row=2, sticky='e'+'w', columnspan=2)
        lDni.grid(column=1, row=3, sticky='e'+'w')
        adni.grid(column=2, row=3, sticky='e'+'w', columnspan=2)

        bGuardar.grid(column=2, row=4, sticky='e'+'w')
        bCancelar.grid(column=3, row=4, sticky='e'+'w')

        alta.grab_set()

        def guardar(nombre1, apellido1, dni1):
            socio1= Socio(dni= int(dni1), nombre= nombre1, apellido= apellido1)
            self.negocio.alta(socio1)
            socio2= self.negocio.buscar_dni(dni1)
            self.tree.insert("", END, text=str(socio2.id), values=(nombre1, apellido1, dni1), iid=socio2.id)
            alta.destroy()

    def baja(self):
        self.negocio.baja(self.tree.focus())
        self.tree.delete(self.tree.focus())

    def modificar(self):
        item = self.tree.selection()
        editar = Toplevel(self.root)
        editar.title("Editar socio")

        lNombre = Label(editar, text="Nombre")
        vNombre = StringVar()
        anombre = Entry(editar, textvariable=vNombre)
        lApellido = Label(editar, text="Apellido")
        vApellido = StringVar()
        aapellido = Entry(editar, textvariable=vApellido)
        lDni = Label(editar, text="Dni")
        vDni= StringVar()
        adni = Entry(editar, textvariable=vDni)
        vNombre.set(self.tree.item(self.tree.focus())['values'][0])
        vApellido.set(self.tree.item(self.tree.focus())['values'][1])
        vDni.set(self.tree.item(self.tree.focus())['values'][2])

        bGuardar = Button(editar, text="Guardar", command=lambda: guardar(item, vNombre.get(), vApellido.get(), vDni.get()), height=1, width=8)
        bCancelar = Button(editar, text="Cancelar", command=lambda: editar.destroy(), height=1, width=8)

        lNombre.grid(column=1, row=1, sticky='e'+'w')
        anombre.grid(column=2, row=1, sticky='e'+'w', columnspan=2)
        lApellido.grid(column=1, row=2, sticky='e'+'w')
        aapellido.grid(column=2, row=2, sticky='e'+'w', columnspan=2)
        lDni.grid(column=1, row=3, sticky='e'+'w')
        adni.grid(column=2, row=3, sticky='e'+'w', columnspan=2)

        bGuardar.grid(column=2, row=4, sticky='e'+'w')
        bCancelar.grid(column=3, row=4, sticky='e'+'w')

        editar.grab_set()

        def guardar(item, nombre1, apellido1, dni1):
            id1= item[0]
            socioN= Socio(id=int(id1), nombre=nombre1, apellido= apellido1, dni= dni1)
            self.negocio.modificacion(socioN)
            self.tree.item(item, text=str(id1), values=(nombre1, apellido1, dni1))
            editar.destroy()


if __name__ == "__main__":
    Presentacion()
