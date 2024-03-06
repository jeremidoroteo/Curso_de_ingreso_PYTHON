import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Jeremi
apellido: Doroteo
---
Ejercicio: if_06
---
Enunciado:
Al presionar el botón 'Calcular', se deberá obtener el contenido de la caja de texto txtEdad, 
transformarlo en número y calcular si es mayor, niño/a(menor de 10) o pre-adolescente 
(edad entre 10 y 13 años) o adolescente (edad entre 13 y 17 años) de edad, 
se deberá informar utilizando el Dialog alert.
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
        
        #region     "DEFINICIONES"
        '''
        ESTRUCTURAS CONDICIONALES MULTIPLES
            Constan de varias condiciones mutuamente excluyentes.
            if condicion1:
                accion1
            elif condicion2: //es la combinacion de else y if
                accion2:
            else: //Siempre va solo, no acepta ninguna condicion.
                accion3
        //Se lee: si pasa la condicion1, entonces hace la accion1, si pasa otra cosa (condicion2), entonces pasa la accion2, y sino pasa nada de las otras condiciones ateriores entonces pasa la accion3...
        
        
        
        ASI QUEDARIA EL EJERCICIO SIN LA CONTRACCION DEL ELSE-IF:

            De esta forma quedaria el "anidamiento";
        
            edad = self.txt_edad.get()
            edad = int(edad)

            if edad < 10:
                mostrar = "El usuario es niño"
            else:
                if edad < 13:
                    mostrar = "El usuario es pre-adolescente"
                else:
                    if edad < 17:
                        mostrar = "El usario es adolescente"
                    else:
                        mostrar = "El usuario es mayor"
            
            alert("Mensaje", mostrar)
        
        
        '''
        #endregion
        
        
        edad = self.txt_edad.get()
        edad = int(edad)

        if edad < 10:
            mostrar = "El usuario es niño"
        elif edad < 13:
            mostrar = "El usuario es pre-adolescente"
        elif edad < 17:
            mostrar = "El usario es adolescente"
        else:
            mostrar = "El usuario es mayor"
        
        alert("Mensaje", mostrar)
    
    #NOTA: El enunciado no deja muy en claro si deberia de incluirse ciertas edades.
        # Como solo dice "entre" no incluí "13" en pre-adolescente, ni "17" en adolescente.
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()