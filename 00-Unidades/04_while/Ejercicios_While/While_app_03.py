import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Jeremi
apellido: Doroteo
---
Ejercicio: while_03
---
Enunciado:
Al presionar el botón ‘Pedir clave’, solicitar al usuario que ingrese una contraseña mediante prompt. 
Comprobar que la contraseña ingresada sea ‘utn750’. En caso de no coincidir, volver a solicitarla hasta que coincidan.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_pedir_clave = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_pedir_clave_on_click)
        self.btn_pedir_clave.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_pedir_clave_on_click(self):
        clave = prompt("Clave", "Ingrese su contraseña: ")
        
        while clave != "utn750":  #otra forma seria while not (clave == "utn750") // pero optimo, pues hay dos operadores relacionales
            clave = prompt("Error", "Reingrese su contraseña: ")
        
        #alert("Mensaje", "Bienvenido") #lo dejo afuera del while porque si no se estaria ejecutando todas las veces que itere el while
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()