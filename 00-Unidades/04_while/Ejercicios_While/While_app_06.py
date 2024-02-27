import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Jeremi
apellido: Doroteo
---
Ejercicio: while_06
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar 5 números mediante prompt. 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

Observacion: para informar los resultados en las cajas de textos es necesario usar insert, ya que seria una salida...
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
        contador_iteracion = 0 #VARIABLE DE CONTROL: cuenta las iteraciones de un while. Por convencion se les puede llamar "i, j, k"
        acumulador_numeros = 0 #ACUMULADOR: acumula los valores que ingresa el usuario
                                #AMBOS SE INICIALIZAN SIEMPRE EN 0
        #antes del while
        
        while contador_iteracion < 5:
            #dentro del while
            numero = prompt("Ingreso", "Ingrese un numero: ")
            numero = int(numero) #parseamos, es decir convertimos un valor de tipo literal a un tipo numerico
            
            acumulador_numeros += numero
            
            
            contador_iteracion += 1 
            
        #fuera del while
        self.txt_suma_acumulada.delete(0, "end") #el primer parametro indica desde que posicion empieza a borrar, y el segundo indica hasta donde, en este caso "end" borraria hasta el final de la linea.
        self.txt_suma_acumulada.insert(0, acumulador_numeros) #(el "." es algo que se desprende del control, se llama metodo, en este caso el metodo insert)
                                        #Basicamente, antes del "." seria datos, y luego del punto serian acciones.
        #"insert" sirve para que el dato que esta dentro de la variable vaya al text box, y no al alert...
            #Necesita dos parametro, a y b. "a" sirve para decir desde que posicion voy a empezar a escribir, por default va 0. Luego, "b" sirve para poner el texto que quiero escribir, en este caso pondria la variable que contiene el texto.  
            #En python la asignacion de variable es destructiva, pues destruye el valor de la variable y crea una nueva (se destruye el espacio de memoria que fue asignada anteriormente, y se crea otra). No puede recordar el numero anterior, solo el ultimo.
            #En este ejercicio estariamos usando un text box para una salida de datos...

        #EL PROMEDIO LO SACAMOS AFUERA DEL WHILE ASI LO HACE SOLO UNA VEZ. Si lo ponemos dentro entonces sacara el promedio de los valores que se van acumulando en cada iteracion, es decir el PROMEDIO PARCIAL, pero luego solo mostraria el promedio final. NO ES NADA OPTIMO
        
        
        promedio = acumulador_numeros / contador_iteracion
        self.txt_promedio.delete(0, "end")
        self.txt_promedio.insert(0, promedio)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
