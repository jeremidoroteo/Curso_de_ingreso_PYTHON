import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Jeremi
apellido: Doroteo
---
Ejercicio: entrada_salida_05
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener tanto el nombre como la edad contenida en 
las cajas de texto correspondientes y luego mostrar los datos concatenados utilizando el Dialog Alert. 
Ej: "Usted se llama José y su edad es 66 años"
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Nombre")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_nombre = customtkinter.CTkEntry(master=self)
        self.txt_nombre.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        
        #region #> "Definiciones"
        '''
        
        TIPOS DE DATOS:
            - String: texto (un literal)
            - Int(er): numeros enteros
            - Float: numeros fraccionarios (con coma) 
        
        - Parsear / Castear: convertir de texto a numero.
        _____________________________________________________
        
        OPERADORES:
            operan; se necesitan 2 elementos (operandos)
            Ejemplo: Su nombre es + nombre  // Concatenacion: es solo para texto (string)
                    operando1 , operador , operando2
                    
        COMO ACTUA EL OPERADOR:
            string + string = concatena
            int + int = suma
            
        OPERADORES ARITMETICOS:
            + : suma
            - : resta
            * : multiplicacion
            / : division
            % : modulo (el resto de la division)
        ________________________________________________________
        
        
        '''

        #endregion
        
        
        nombre = self.txt_nombre.get()
        edad = self.txt_edad.get()
        mensaje = "Usted se llama " + nombre + " y su edad es " + edad + " años"
        alert("Datos", mensaje)

        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()