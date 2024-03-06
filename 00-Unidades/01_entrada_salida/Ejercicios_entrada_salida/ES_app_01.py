import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Jeremi
apellido: Doroteo
---
Ejercicio: entrada_salida_01
---
Enunciado:
Al presionar el  botón, se debe mostrar un mensaje como el siguiente "Esto no anda, funciona".
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        
        #region #> "Definiciones"
        '''
        PARTES DE UN ALGORITMO:
            -Entrada: con que tipo de dato voy a trabajar
            -Procesos: que quiero hacer con esos tipos de datos
            -Salidas: que necesito ver como un resultado
            
        -Indentacion: es una sangria e indica los niveles de promacion (prioridad).
        
        FUCIONES:
            -alert("a", "b"): es una ventana emergente, permite mostrar un mensaje y sirve para interactuar. Tiene 2 parametros,a y b.
                a: titulo de la ventana // b: el mensaje que se quiere mostrar // Ambos estan entre comillas porque son valores literales.
        
        '''        
        #endregion
        
                
        alert("titulo","esto no anda, funciona")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
