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
        
        seguir = True
        
        contador_masculino_iot_ia = 0
        
        contador_ia = 0
        contador_iot = 0
        contador_rv_ra = 0
        
        contador_masculino = 0
        contador_femenino = 0
        contador_otro = 0
        
        while seguir:
            #Ingreso de datos y validaciones
            nombre = prompt("Nombre", "Ingrese su nombre: ")
            edad = prompt("Edad", "Ingrese su edad: ")
            edad = int(edad)
            
            while edad < 18:
                edad = prompt("Invalido", "Reingrese su edad: ")
                edad = int(edad)
            
            genero = prompt("Genero", "Ingrese su genero: Masculino - Femenino - Otro ")
            
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":  #Va "and" porque se tiene que cumplir que no es ninguno de lo que esta enunciado ahi... Si pongo "or" si se cumple que es distinto al primero entonces no valida los otros casos...
                genero = prompt("Invalido", "Reingrese su genero: Masculino - Femenino - Otro ")
                
            tecnologia = prompt("Tecnologia", "Ingrese Tecnologia: IA - RV/RA - IOT")
            
            while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
                tecnologia = prompt("Tecnologia", "ngrese Tecnologia: IA - RV/RA - IOT")
            
            '''    
            if tecnologia == "IOT":
                contador_iot += 1
            
            elif tecnologia == "IA":   #va elif porque todas son condiciones autoexcluyentes, no puede elegir 2 cosas al mismo tiempo...
                contador_ia += 1
            
            else:
                contador_rv_ra += 1
                
                Se podia hacer con if tambien, pero lo vamos a hacer con match...
            '''
            match tecnologia:
                case "IOT":
                    contador_iot += 1
                
                case "IA":
                    contador_ia += 1
                
                case "RV/RA":
                    contador_rv_ra += 1
                        
            
            match genero:
                case "Masculino":
                    contador_masculino += 1
                    if (tecnologia == "IOT" or tecnologia == "IA") and (edad >= 25 and edad <=50):
                        contador_masculino_iot_ia += 1
                        
                case "Femenino":
                    contador_femenino += 1
                
                case "Otro":
                    contador_otro += 1
            
            
            #Procesamiento de datos dentro del while
            
            #if genero == "Masculino" and (tecnologia == "IOT" or tecnologia == "IA") and (edad >= 25 and edad <=50):
                #contador_masculino_iot_ia += 1
            
            #borre todo esto y lo meti en el match xd
            
            
            
            
        #seguir = question("Seguir", "Desea continuar?")
        
        
        #Procesos fuera del while
        
        if contador_ia > contador_rv_ra and contador_ia > contador_iot:
            print("Se voto mas IA")
        
        elif contador_rv_ra > contador_iot:
            print("Se voto mas RV/RA")
        
        else:
            print("Se voto mas IOT")
            
        #OBSERVACION: acotamos este ejercicio, de manera que pensamos que todos los contadores son distintos, pues asi descartariamos muchas otras posibilidades...
        
        total_empleados = contador_masculino + contador_femenino + contador_otro
        porcentaje_masculinos = (contador_masculino * 100) / total_empleados
        porcentaje_femeninos = (contador_femenino * 100) / total_empleados
        #porcentaje_otro = (contador_otro * 100) / total_empleados      Una manera de hacer
        porcentanje_otro = 100 - (porcentaje_masculinos + porcentaje_femeninos)
        
        #OBSERVACION:
            #Al procesador le cuesta mas hacer una resta que una suma, por eso sumamos los porcentajes en vez de restar todos...
            
        
        
        
        #Salidas (informes)
        print(f"1. Cantidad de empleados masculinos IOT/IA entre 25 y 50: {contador_masculino_iot_ia}")
        
        print(f"Porcentajes: \n\tFemenino: {porcentaje_femeninos}%\n\tMasculino: {porcentaje_masculinos}%\n\tOtro: {porcentanje_otro}%")
        
        
        '''
        #DEFINICION
            #question("a", "b") // es parecido a un alert y un prompt. a: es un titulo. b: el mensaje
                #Es una forma de trabajar con el escape (huida) del while para cuando no sabemos cuantas iteraciones vamos a realizar
                #Es una alternativa para no usar banderas
            
            #!= // significa distinto
            
            #\n // salto de linea
            
            #\t // tabulacion (sangria)

        #TIP
            #A medida que voy programando cada variable voy validando... Pido el dato y ahi mismo valido
    
        #TIP COMANDO
            #Seleccionar una palabra: ctr + shift + flecha izquierda o derecha
            
            #Cambiar varias palabras que son iguales al mismo tiempo: me posiciono en la primera palabra y presiono ctr + d. Sigo presionando va seleccionando todas las mismas palabras hacia la derecha...
            
        #EN UNA VALIDACION SE PREGUNTA POR LO QUE NO QUIERO QUE SE CUMPLA... EJEMPLO EN WHILE
        '''
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
