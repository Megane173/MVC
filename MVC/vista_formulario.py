

class Vista:

    def __init__(self, titulo="Validar numeros", pregunta1="Digite el numero: ", entrada1="", opciones=["Ver si un numero es par o impar","Ver si numero es positivo o negativo o neutro"], entry_menu="-1"):

        self.titulo=titulo
        self.pregunta1=pregunta1
        self.entrada1=entrada1
        self.opciones=opciones
        self.entry_menu=entry_menu
        
    def get_entry_menu(self):
        return self.entry_menu

    def mostrar_menu(self):
        
        for i in range(2):
            print("-("+str(i+1)+") "+str(self.opciones[i]))
            
        print("(-1) Salir")
        
        self.entry_menu=input("Digite el numero de acuerdo a la accion que quiere hacer: ")
        return self.entry_menu
        
    def hacer_campo(self):
        print(self.titulo)
        print(self.pregunta1+": ")
        self.entrada1 = int(input())
        return self.entrada1
        

    def imprimir(self, dato_mensaje):
        print(dato_mensaje)
