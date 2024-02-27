import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Jeremi
apellido: Doroteo
---
Ejercicio: while_09
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera 
hasta que presione el botón Cancelar (en el prompt). 
Luego determinar el máximo y el mínimo 
e informarlos en los cuadros de textos txt_maximo y txt_minimo respectivamente

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.txt_minimo = customtkinter.CTkEntry(
            master=self, placeholder_text="Mínimo")
        self.txt_minimo.grid(row=0, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(
            master=self, placeholder_text="Máximo")
        self.txt_maximo.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20,
                            columnspan=2, sticky="nsew")

    def btn_comenzar_ingreso_on_click(self):
        
        maximo = 0
        minimo = 0
        #Si quiero optimizar el recurso, entonces tengo que declarar las variables, es decir dar un valor inicial
        
        bandera_primero_ingreso = False
        
        while True:
            numero = prompt("Numeros", "Ingrese un numero: ")
        
            if numero == None:
                break
            
            numero = int(numero)
            
            if numero > maximo or bandera_primero_ingreso == False: #Si esta en False entonces quiere decir que recien estoy por hacer el primer ingreso
                maximo = numero
            
            if numero < minimo or bandera_primero_ingreso == False:
                minimo = numero
                
                bandera_primero_ingreso = True  #Se ejecuta solo cuando encuentra 1 Mínimo
                
                
            #bandera_primero_ingreso = True // Se ejecuta siempre // Faltaba optimizar, para que se ejecute solo cuando encuentre 1 Minimo... es decir, reducimos la cantidad de veces que podria haberse ejecutado
        
        #Forma mas ridumentaria de calcular Maximos y Minimos:
            #Nuestro programa no tiene la capacidad de recordar cuales son todos los numeros que ingresé, entonces este algoritmo tiene que preguntar por cada numero respecto al anterior si es Max o Min y luego ir recordando
        
        #DEFINICIONES:
            #true // nos permite que el while se ejecute reiteradas veces
        
            #break // permite cortar la iteracion. Es un corte de control
        
            #bandera o flag // guarda un estado cualquiera.  Es una variable de cualquier naturaleza (entero, cadena, booleano, etc). Sirve para reducir el impacto en el procesador
            #Incializamos en "False" porque seria en el sentido semantico que no ocurrió el primer ingreso
            
            #setear // refiere a asigar un valor a una variable
        
            #None // significa valor nulo... denota ausencia de valor o valor desconocido
            
            #Castear // convertir un tipo de variable a otro
            
            #= // operador de asignacion
            
            #== // operador de comparacion

        #OBSERVACIONES:
        #el contador unicamente se utiliza si necesitamos sacar algun promedio, si no, no


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()


'''    
    VERSION 1:
    
            while contador < 5:
                numero = prompt("Numeros", "Ingrese numero: ")
                numero = int(numero)
                
                if contador == 0:
                    maximo = numero
                    minimo = numero
                    
                else:
                    if numero > maximo:
                        maximo = numero
                    
                    if numero < minimo:
                        minimo = numero
                
                
                contador += 1

            NOTA: no estaria optimizado, pues se preguntaria todo el tiempo si contador es igual a 0
            

    VERSION 2:
    
            contador = 0
            
            maximo = 0
            minimo = 0
            
            while contador < 5:
                numero = prompt("Numeros", "Ingre un numero: ")
                numero = int(numero)
                
                if numero > maximo or contador == 0:
                    maximo = numero
                
                if numero < minimo or contador == 0:
                    minimo = numero
                    
            
                contador += 1

            NOTA: No está totalmente optimizada, y ademas solo tiene un limite de 5 numeros.
            
            NOTA 2: Ponemos "contador == 0" del lado derecho asi el programa no pregunta todo el tiempo esa instruccion...
                    Aunque podria pasar que pregunte alguna que otra vez, pero al menos reducimos la cantidad de veces que podria preguntar...

'''                