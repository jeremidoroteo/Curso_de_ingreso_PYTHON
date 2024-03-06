import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Jeremi
apellido: Doroteo
---
Ejercicio: if_07
---
Enunciado:
Los argentinos nativos y por opción desde los dieciséis (16) años y los argentinos
naturalizados desde los dieciocho (18) años están habilitados a votar. 
Al presionar el botón 'Mostrar', se deberá informar (utilizando el Dialog Alert) 
si es o no posible que la persona concurra a votar en base a la información 
suministrada.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Tipo")
        self.label2.grid(row=1, column=0, padx=20, pady=10)

        self.combobox_tipo = customtkinter.CTkComboBox(master=self, values=["NATIVO", "NATURALIZADO"])
        self.combobox_tipo.grid(row=1, column=1, padx=20, pady=10)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        
        #region     "DEFINICIONES"
        '''
        - ComboBox: permite seleccionar un elemento de una lista despegable de valores.
            - Se utiliza junto con el metodo ".get" para extraer el valor.
            - Devuelve un String.
        
        
        OBERVACION
            Tanto el "and" como el "or" funcionan como cortocircuito.
            Por ejemplo, si una sola concion en el "and" es false, entonces todo es false, porque para que "and" sea True, todas las condiciones deben ser True.

            Luego, en el "or" con que una condicion se cumpla, entonces todo el if es True, y se ejecuta el codigo.
        
        '''
        #endregion
        

        edad = self.txt_edad.get()
        edad = int(edad)
        
        tipo = self.combobox_tipo.get()
        
        if (edad >= 16 and tipo == "NATIVO") or (edad >= 18 and tipo == "NATURALIZADO"):
            mostrar = "Puede votar"
        
        else:
            mostrar = "No puede votar"
        
        alert("Mensaje", mostrar)
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()