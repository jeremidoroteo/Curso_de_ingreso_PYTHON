import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''

nombre: Jeremi
apellido: Doroteo
---
Ejercicio: Match_01
---
Enunciado:
Obtener el valor del mes seleccionado en el combobox_mes y  
al presionar el botón ‘Informar’ mostrar mediante alert los siguientes mensajes 
en función del mes seleccionado:
    Si el mes seleccionado es Enero: ‘que comiences bien el año!!!’
    Si el mes seleccionado es Marzo: ‘a clases!!’
    Si el mes seleccionado es Julio: ‘se vienen las vacaciones!!’
    Si el mes seleccionado es Diciembre: ‘Felices fiestas!!!’

En caso de seleccionar un mes distinto a los mencionados, no hacer nada
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label_meses = customtkinter.CTkLabel(master=self, text="Meses")
        self.label_meses.grid(row=0, column=0, padx=20, pady=10)
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        self.combobox_mes = customtkinter.CTkComboBox(master=self, values=meses)
        self.combobox_mes.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        
        #region     #DEFINICIONES
        '''
        Match (variable):
            case 1:
                accion1
            case 2: accion2
            case _: // Es el caso default, los casos restantes... como el else en el if
                accion3
        
        // Match evalua el valor de una variable, y compara con cada valor de cada caso...
        
        // Se lee: si se cumple el caso1, entonces pasa la accion1, si se cumple el caso2, entonces pasa la accion2, si no sucede ninguno de los casos, entonces sucede el caso default y pasa la accion3.
        
        '''
        #endregion
        
        
        mes = self.combobox_mes.get()
        
        match (mes):
            case "Enero":
                informar = "Que comiences bien el año"
                alert("Informe", informar)
                
            case "Marzo":
                informar = "A clases!!"
                alert("Informe", informar)
                
            case "Julio":
                informar = "Se vienen las vacaciones"
                alert("Informe", informar)
                
            case "Diciembre":
                informar = "Felices Fiestas!!!"
                alert("Informe", informar)
                
        
    
    #Como dice no hacer nada literalmente... entonces tengo que colocar un alert en cada case... porque si declaro la variable "informar" antes, mostraria un mensaje vacio, pero estaria mostrando algo.
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()