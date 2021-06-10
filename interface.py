import tkinter
import C_temperatura

ventana = tkinter.Tk()
ventana.geometry('500x500')

#Nombre de la ventana
ventana.title('Calculadora Magica')

#Encabezado de la aplicacion
texto = tkinter.Label(ventana, text = 'Calculadora Magica')
texto.pack()

def eleccion(numero):
    print(numero)
    if numero == 1:
        print("Calculadora de Temperatura")

        #Llammos al modulo de C_Temperatura
        C_temperatura.ventanita()
        
    if numero == 2:
        print("Calculadora de Calorias")

    if numero == 3:
        print ("Calculadora de Porcentaje")

    if numero == 4:
        print("Tu peso en Otro Planeta")

boton1 = tkinter.Button(ventana, text = 'Calculadora de Temperatura', command = lambda: eleccion(1))
boton1.pack()

boton2 = tkinter.Button(ventana, text = 'Calculadora de Calorias', command = lambda: eleccion(2))
boton2.pack()

boton3 = tkinter.Button(ventana, text = 'Calculadora de Porcentaje', command = lambda: eleccion(3))
boton3.pack()

boton4 = tkinter.Button(ventana, text = 'Tu peso en Otro Planeta', command = lambda: eleccion(4))
boton4.pack()

ventana.mainloop()