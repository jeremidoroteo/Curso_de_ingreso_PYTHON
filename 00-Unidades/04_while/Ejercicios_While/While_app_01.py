import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Jeremi
apellido: Doroteo
---
Ejercicio: while_01
---
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert 
10 repeticiones con números ASCENDENTE desde el 1 al 10
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        
        #region     DEFINICIONES
        '''
        ESTRUCTURAS REPETITIVAS
            trabaja en bucle, permite repetir una accion o un conjunto de acciones las cantidades de veces que quiero
            
            while condicion:
                sentencias a repetir
                
        
        //El while permite ejecutar un codigo mientras la condicion se cumpla, cuando se deja de cumplir, sale del bucle y continua su ejecucion normal
        //Cada que se ejecuta una vez la sentencia, eso se llama iteracion. Luego se vuelve a evaluar la condicion, si es True, entonces nuevamente vuelve a iterar
        // Dentro de la sentencia debe haber por lo menos 1 que haga la condicion falsa, asi puede salir del bucle, si no seria un bucle infinito...
        
        
        - Contador: sirve para contar. Tomamos un valor base y lo incrementamos con el mismo elemento, es decir un incremento constante.
            Ejemplo: contador = 1 
                        contador += 1 // Incrementa de 1 en 1 el contador
        
        - Acumulador: acumulan valores. No es constante...
        
        
        
        '''
        #endregion
        
        
        contador_iteracion = 0
        
        while contador_iteracion < 10:
            print(contador_iteracion + 1)
            #contador_iteracion = contador_iteracion +1 #incremento de la variable de control
            contador_iteracion += 1
            
            
    print("Holaa")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()