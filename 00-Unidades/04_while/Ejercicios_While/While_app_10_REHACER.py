import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: De practica que dio Ger...
---
Enunciado:

UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
que promete revolucionar el mercado. 
Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT)

Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

Los datos a ingresar por cada encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT)   

En esta opción, se ingresaran empleados hasta que el usuario lo desee.

Una vez finalizado el ingreso, mostrar:

    #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #!X 2) - Tecnología que mas se votó.
    #!X 3) - Porcentaje de empleados por cada genero
    #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.
    
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        
        #region #> "ENUNCIADO"
        '''
        Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

        Los datos a ingresar por cada encuestado son:
        * nombre del empleado
        * edad (no menor a 18)
        * genero (Masculino - Femenino - Otro)
        * tecnologia (IA, RV/RA, IOT)   

        En esta opción, se ingresaran empleados hasta que el usuario lo desee.

        Una vez finalizado el ingreso, mostrar:

        #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
        #!X 2) - Tecnología que mas se votó.
        #!X 3) - Porcentaje de empleados por cada genero
        #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
        #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
        #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.
        
        '''
        #endregion
        
        
        #region #> "Inicializaciones"
        
        seguir = True # es una bandera, le asigamos un booleano
        
        #endregion
        
        
        while seguir:
            #region #> "Entradas"
            
            nombre = input("Ingrese nombre: ")
            
            edad = input("Ingrese edad: ")
            edad = int(edad)
            
            while edad < 18:
                edad = input("Reingrese edad: ")
                edad = int(edad)
            
            genero = input("Ingrese genero: Masculino - Femenino - Otro")
            while genero != "Masculino" and genero != "Femenino" and genero != Otro:
                genero = input("Reingrese genero: Masculino - Femenino - Otro")
                
            tecnologia = input("Ingrese tecnologia: IA - RV/RA - IOT")
            while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
                tecnologia = input("Reingrese tecnologia: IA - RV/RA - IOT")
                
            #endregion
            
            
            #region #> "Procesos dentro del while"
            
            
            
            
            
            
            
            
            
            
            
            
            seguir = question("Desea ingresar otro?")
            #endregion
            
            
        #region #> "Procesos afuera del while"
        
        #endregion
        
            
        #region #> "Salidas"
        
        #endregion
        
            
                
            
            
            
            
            
            
    #region #> "Conceptos"
    '''
    Booleano // representa un valor de verdad: True or False
    
    '''
    #endregion        
            
    
    
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
