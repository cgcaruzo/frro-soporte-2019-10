## 1 Ejercicio Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
## Y 4 botones de operaciones para las operaciones respectivas + , - , * , / ,
## al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 .

from tkinter import *

def operacion(op):
    if op == 1:
        numRes.set(numV1.get()+numV2.get())
    if op == 2:
        numRes.set(numV1.get()-numV2.get())
    if op == 3:
        numRes.set(numV1.get()*numV2.get())
    if op == 4:
        numRes.set(numV1.get()/numV2.get())

root = Tk()
root.title("Ventana principal")

lblV1 = Label(root, text="Valor 1")
numV1 = IntVar()
entV1 = Entry(root, textvariable=numV1)

lblV2 = Label(root, text="Valor 2")
numV2 = IntVar()
entV2 = Entry(root, textvariable=numV2)

lblRes = Label(root, text="Resultado")
numRes = IntVar()
entRes = Entry(root, textvariable=numRes)

btnSum = Button(root, text="+", command=lambda: operacion(1))
btnRes = Button(root, text="-", command=lambda: operacion(2))
btnMult = Button(root, text="x", command=lambda: operacion(3))
btnDiv = Button(root, text="/", command=lambda: operacion(4))

lblV1.grid(column=1, row=1)
entV1.grid(column=2, row=1)
lblV2.grid(column=1, row=2)
entV2.grid(column=2, row=2)
lblRes.grid(column=1, row=3)
entRes.grid(column=2, row=3)
btnSum.grid(column=3, row=1)
btnRes.grid(column=4, row=1)
btnMult.grid(column=5, row=1)
btnDiv.grid(column=6, row=1)

root.mainloop()