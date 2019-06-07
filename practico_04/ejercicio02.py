## 2 Ejercicio Hacer un formulario en Tkinter una calculadora que tenga 1 entry y 12 botones para los dígitos 0 al 9
## y las operaciones + - / * = , que al apretar cada botón vaya agregando al valor que muestra en el entry el carácter
## que le corresponde ( como se ve imagen ) y cuando se aprieta en = pone el resultado de evaluar la cadena entrada .

from tkinter import *
from tkinter import ttk

def addSimbol(sim):
    print(sim)
    entrada.set(entrada.get()+str(sim))
    pass

def resolver():
    pass
root = Tk()
root.title("Calculadora")
root.resizable(False, False)
entrada = StringVar()
entRes = Entry(root, textvariable=entrada)
digitos = [0,1,2,3,4,5,6,7,8,9]
operaciones = ['+','-','x','/']
botones = []

for i in digitos:
    print(i)
    botones.append(Button(root, text=str(i), command=lambda sim = i: addSimbol(sim)))

for i in operaciones:
    print(i)
    botones.append(Button(root, text=str(i), command=lambda sim = i: addSimbol(sim)))

botones.append(Button(root, text="=", command=lambda: resolver()))

entRes.grid(row=1, column=1, padx=2, pady=2, sticky='we', columnspan=4)

botones[7].grid(row=2, column=1, sticky='e'+'w', padx=2, pady=2)
botones[8].grid(row=2, column=2, sticky='e'+'w', padx=2, pady=2)
botones[9].grid(row=2, column=3, sticky='e'+'w', padx=2, pady=2)
botones[4].grid(row=3, column=1, sticky='e'+'w', padx=2, pady=2)
botones[5].grid(row=3, column=2, sticky='e'+'w', padx=2, pady=2)
botones[6].grid(row=3, column=3, sticky='e'+'w', padx=2, pady=2)
botones[1].grid(row=4, column=1, sticky='e'+'w', padx=2, pady=2)
botones[2].grid(row=4, column=2, sticky='e'+'w', padx=2, pady=2)
botones[3].grid(row=4, column=3, sticky='e'+'w', padx=2, pady=2)
botones[0].grid(row=5, column=1, sticky='e'+'w', padx=2, pady=2)

botones[10].grid(row=2, column=4, sticky='e'+'w', padx=2, pady=2) #suma
botones[11].grid(row=3, column=4, sticky='e'+'w', padx=2, pady=2) #resta
botones[13].grid(row=4, column=4, sticky='e'+'w', padx=2, pady=2) #division
botones[12].grid(row=5, column=4, sticky='e'+'w', padx=2, pady=2) #multiplicacion

botones[14].grid(row=5, column=2, sticky='e'+'w', padx=2, pady=2, columnspan=2)

root.mainloop()