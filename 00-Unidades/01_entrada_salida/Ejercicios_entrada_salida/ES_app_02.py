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
        
        #region #> "Definiciones"
        '''
        
        - snake_case: identificador que acepta python. Ejem: nombre_alumno

        - lower camel case: se acepta en otros lenguajes. Ejemplo: nombreAlumnoRepropado
        
        - variable: elemento que sirve para guardar datos (son porciones de memoria).
                    Se asigna un valor a la variable con el operador " = "
                    Crear una variable y darle un valor se le dice "harcodear o asignar" un valor.
        // En Python las variables existen cuando las declaramos. Se puede declarar y usarla al mismo tiempo.
        
        - prompt("a", "b"): es parecido al alert (una ventana emergente), pero espera a que el usuario ingrese un dato y devuelve lo que haya ingresado a la variable. Ej: si pone Juan, devuelve Juan
            Paramatros:
                a: titulo. 
                b: instrucion. Es el mensaje que le quiero dar al usuario
        // A diferencia del alert, el prompt esta asignado a algo. La asignacion se resuelve de derecha a izquierda; tengo que tener una variable que ataje el valor que devuelve el prompt
        

        // Prompt para generar una entrada (escribo en una pedacito de memoria), y alert para mostrar un dato (leyendo un pedacito de memoria) (salida).
        
        //La ejecucion de los programas por ahora es secuencial, una cosa debajo de la otra.
        
        
        // DAR FORMATO A UN TEXTO
            El mas eficiente y facil:
            - interpolando texto: dentro de un literal voy a meter un valor de una variable. Hay que indicar al string que esto es un string con formato, entonces adelante de la cadena pongo la letra "f".
                Ejemplo: f"Usted se llama: {nombre de variable}"
                
            - concatenando texto: se unen o se juntan con el operador "+", y se parsea el valor de la variable a un string...
                Ejemplo: "Usted se llama + str(nombre de la variable)"

        
        '''
        
        #endregion
        
        

        nombre_alumno = prompt("Datos","Ingrese su nombre")
        alert("Datos", nombre_alumno)


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()