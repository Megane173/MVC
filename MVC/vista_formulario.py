

class Vista:

    def __init__(self, titulo="Validar numeros", pregunta_campo_numero="Digite el numero", campo_dato_numero=""):

        self.titulo=titulo
        self.pregunta_campo_numero=pregunta_campo_numero
        self.campo_dato_numero=campo_dato_numero


    def hacer_campo(self):
        print(self.titulo)
        print(self.pregunta_campo_numero+": ")
        print(self.campo_dato_numero)
        self.campo_dato_numero = int(input())
        return self.campo_dato_numero
        

    def imprimir(self, dato_mensaje):
        print(dato_mensaje)