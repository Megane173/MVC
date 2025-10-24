


class Controlador:

    def __init__(self, modelo="", vista=""):
        self.modelo=modelo
        self.vista=vista

    def get_modelo(self):
        return self.modelo
    def set_modelo(self, modelo):
        self.modelo=modelo

    def get_vista(self):
        return self.vista
    def set_vista(self, vista):
        self.vista=vista
        
    def mostrar_menu(self):
        
        eleccion=self.vista.mostrar_menu()
        if(eleccion=="-1"):
            self.vista.imprimir("Saliendo...")
        elif(eleccion!=1 or eleccion!=2):
            self.vista.imprimir("\nDigito un caracter que no esta asociado a ninguna opcion.")
        else:
            self.completar_accion(eleccion)
            
    def pedir_numero(self):
        numero=self.vista.hacer_campo()
        self.modelo.set_numero(numero)
        
    def completar_accion(self, eleccion):
        
        self.pedir_numero()
        
        msg="abd"
        
        if(eleccion=="1"):
            msg=self.modelo.es_par()
        elif(eleccion=="2"):
            msg=self.modelo.es_positivo()  
        msg+="\n"
        
        self.mostrar_resultado(msg)
        

    def mostrar_resultado(self, msg):
        self.vista.imprimir(msg)
