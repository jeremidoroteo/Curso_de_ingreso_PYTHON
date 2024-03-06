import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Jeremi
apellido: Doroteo
---
Ejercicio: entrada_salida_03
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener el contenido de la caja de texto para luego 
mostrarlo utilizando el Dialog Alert
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Nombre")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_nombre = customtkinter.CTkEntry(master=self)
        self.txt_nombre.grid(row=0, column=1)
        
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        
        #region #> "Definiciones"
        '''
        
        self.text_nombre: componente del cual quiero traer un dato (caja de texto)
            - Para obtener el contenido de este text box se usa ".get". Devuelve el contenido que ingresó el usuario.
            - El ".get" (es un metodo) sirve para mostrar un contenido especifico del text box. Si no escrito eso, entonces a la variable le estaria pasando todo el text box...
        
        '''
        
        #endregion


        nombre = self.txt_nombre.get()
        alert("titulo", nombre)
                
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()