

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

    def construir_pregunta(self):

        dato_numero=self.vista.hacer_campo()
        self.modelo.set_numero(dato_numero)

    def validar_numero(self):

        msg=self.modelo.validar_numero()
        self.vista.imprimir(msg)
