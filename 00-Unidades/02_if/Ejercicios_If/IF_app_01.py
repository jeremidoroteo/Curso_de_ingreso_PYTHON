import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Jeremi
apellido: Doroteo
---
Ejercicio: if_01
---
Enunciado:
Al presionar el botón 'Mostrar', se deberá obtener el contenido de la caja de texto txt_edad,
transformarlo en número, si coincide con el valor 18, mostrar el mensaje “Usted tiene 18 años” utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        
        #region #> "Definiciones"
        
        '''
        OPERADORES RELACIONALES
            Se emplea para comparar dos elemenos. Devuelve un valo booleano (T o F)
            > : devuelve T si el operador de la izquierda es mayor que el de la derecha
            < : devuelve T si el operador de la izquierda es menor que el de la derecha
            == : devuelve True si ambos operandos son iguales
            >= : devuelve T si el operador de la izquierda es mayor o igual que el de la derecha
            <= : devuelve T si el operador de la izquierda es menor o igual que el de la derecha
            != : devuelve T si ambos operandos no son iguales (distintos)
            
        Observacion: devuelve True cuando la "boquita" come al numero mayor...
            Tanto el "==" y el "!=" se puede usar para comparar strings
        
        ESTRUCTURA CONDICIONAL SIMPLE
            if condicion:
                accion(sentencia)
        
        
        '''
        #endregion
        
        
        edad = self.txt_edad.get()
        edad = int(edad)
        
        if edad == 18:
            alert("Mensaje", "Usted tiene 18 años")
            
        
        
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()