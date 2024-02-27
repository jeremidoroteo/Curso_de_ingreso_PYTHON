import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Jeremi
apellido: Doroteo
---
Ejercicio: while_07
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera, 
hasta que presione el botón Cancelar (en el prompt). 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        pass
        #Dato: El prompt devuelve un "None" (un nulo) cuando presiono cancelar
        #Dato2: El input sirve para poner un valor y devuelve un valor, pero todo por consola
        
        '''PRUEBA DE "NONE":
        
        METODO 1:
        
        valor = prompt("titulo", "Ingrese :")
        valor = int(valor)
        
        if valor == None
            alert("lalal", "NONE")
            
        elif valor == 4:
            alert("lalal", "VALOR")
            
            // De esta forma no se podrá parsear el valor "none". Entonces, es mejor usar un else y luego if
            
        METODO 2:  

        valor = prompt("titulo", "Ingrese :")
        
        if valor == None
            alert("lalal", "NONE")
            
        else:
            valor = int(valor)
            if valor == 4:
                alert("lalal", "VALOR")
            
                //Aca si es un valor distinto a "None" Entonces si podra parsearlo a un valor entero
        
        '''

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
