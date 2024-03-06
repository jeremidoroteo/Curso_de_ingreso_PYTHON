import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Jeremi
apellido: Doroteo
---
Ejercicio: Simulacro de examen
---
Enunciado:
Un famoso casino de mar del plata,  requiere una app para controlar el egreso de dinero durante una jornada. Para ello se ingresa por cada ganador:

    Nombre

    Importe ganado (mayor o igual $1000)

    Género (“Femenino”, “Masculino”, “Otro”)

    Juego (Ruleta, Poker, Tragamonedas)

Necesitamos saber:

1. Nombre y género de la persona que más ganó.

2. Promedio de dinero ganado en Ruleta.

3. Porcentaje de personas que jugaron en el Tragamonedas.

4. Cuál es el juego menos elegido por los ganadores.

5. Promedio de importe ganado de las personas que NO jugaron Poker, siempre y cuando el importe supere los $15000

6. Porcentaje de dinero en función de cada juego

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        
        contador_ruleta = 0
        contador_poker = 0
        contador_tragamonedas = 0
        
        importe_ganado_ruleta = 0
        importe_ganado_poker = 0
        importe_ganado_tragamonedas = 0
        
        contador_femenino = 0
        contador_masculino = 0
        contador_otro = 0
        
        
        
        seguir = True
        
        while seguir:
            
            nombre = input("Ingrese un nombre:  ")
            
            importe_ganado = input("Ingrese importe:    ")
            importe_ganado = float(importe_ganado)
            
            while importe_ganado < 1000:
                importe_ganado = input("Reingrese un importe:   ")
                importe_ganado = int(importe_ganado)
            
            genero = input("Ingrese genero: Femenino - Masculino - Otro\n")
            
            while genero != "Femenino" and genero != "Masculino" and genero != "Otro":
                genero = input("Reingrese genero: Femenino - Masculino - Otro\n")
            
            juego = input("Ingrese un juego: Ruleta - Poker - Tragamonedas\n" )
            while juego != "Ruleta" and juego != "Poker" and juego != "Tragamonedas":
                juego = input("Reingrese un juego: Ruleta - Poker - Tragamonedas\n" )
                
            
            
            


            match juego:
                case "Ruleta":
                    contador_ruleta += 1
                    importe_ganado_ruleta += importe_ganado
                    
                case "Poker":
                    contador_poker += 1
                    importe_ganado_poker += importe_ganado
                    
                case "Tragamonedas":
                    contador_tragamonedas += 1
                    importe_ganado_tragamonedas += importe_ganado
            
                
                    
                    
                    
                    
            match genero:
                case "Femenino":
                    contador_femenino += 1
                case "Masculino":
                    contador_masculino += 1
                case "Otro":
                    contador_otro += 1
            
            
            
            
            
            
            
            
            

            avanzar = question("avanzar", "Desea avanzar?")


        
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()


'''
OBSERVACIONES
    El booleano al estar en una variable "seguir", con otra instruccion (question) nos permite cambiar el valor, a False por ejemplo, para romper el bucle en algun momento.
    



CONCEPTOS:




'''