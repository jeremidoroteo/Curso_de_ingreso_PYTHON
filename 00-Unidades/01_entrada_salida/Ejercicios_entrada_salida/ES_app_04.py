import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Jeremi
apellido: Doroteo
---
Ejercicio: entrada_salida_04
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un nombre utilizando el Dialog Prompt 
y luego mostrarlo en la caja de texto txt_nombre (.delete / .insert )
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
        Alternativas para borrar la caja, pero no tan eficientes:
            #self.text_nombre.delete(0, 30)
            #self.text_nombre.delete(0, tkinter.END)
            #self.text_nombre.delete(0, len(self.txt_nombre.get()))

        .delete(a, b): borra, elimina, limpia el contenido del text box.
            - a: desde donde quiero borrar.
            - b: hasta donde quiero borrar.
            // El mas optimo es este: .delete(0, "end")
        
        .insert(a, b): es una accion al igual que el ".get".
            - Parametros: 
                - a: indica desde que posicion del text box voy a empzar a escribir, por default se pone 0.
                - b: es el texto que quiero escribir. Si el texto está en una variable, entonces pongo el nombre de la variable.

        //Las cajas de textos serian controles (datos), y el .algo seria metodos (acciones) que se desprenden de esos controles...
        
        // UN TEXT BOX NOS SIRVE PARA GENERAR ENTRADAS Y TAMBIEN GENERAR SALIDAS
        // EN ESTE CASO USAMOS UN TEXT BOX PARA UNA SALIDA DE DATOS
        
        '''
        
        #endregion

        nombre_alumno = prompt("Titulo","Ingrese el nombre") 
        self.txt_nombre.insert(0, nombre_alumno)
        self.txt_nombre.delete(0, "end")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()