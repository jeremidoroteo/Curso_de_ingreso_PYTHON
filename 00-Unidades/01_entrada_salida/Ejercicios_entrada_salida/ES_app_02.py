import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Jeremi
apellido: Doroteo
---
Ejercicio: entrada_salida_02
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un dato utilizando el Dialog Prompt
y luego mostrarlo utilizando el Dialog Alert
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        
        #snake_case (identificador que acepta python*)
        # En Python las variables existen cuando las declaramos. Se puede declarar y usarla al mismo tiempo.
            #Se asigna un valor a la variable con el operador " = "

        nombre_alumno = prompt("Datos","Ingrese su nombre")
        alert("Datos", nombre_alumno)

        #El "prompt" es parecido al alert, pero espera a que el usuario ingrese un dato y devuelve lo que haya ingresado a la variable. Ej: si pone Juan, devuelve Juan
            #El prompt recibe 2 paramaetros ("titulo", "instrucion"). La instruccion es el mensaje que le quiero dar al usuario
            #A diferencia del alert, el promp esta asignado a algo. La asignacion se resuelve de derecha a izquierda; tengo que tener una variable que ataje el valor que devuelve el prompt
        #En el 2do parametro del "alert" se pone la variable (sin comillas)

        # Prompt para generar una entrada (escribo en una pedacito de memoria), y alert para mostrar un dato (leyendo un pedacito de memoria).


        nombreAlumnoRepropado
        #lower camel case (se acepta en otros lenguajes)
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()