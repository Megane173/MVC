

class Numero:

    def __init__(self, numero=" "):
        self.numero=numero

    def get_numero(self):
        return self.numero
    
    def set_numero(self, numero):
        self.numero=numero


    def validar_numero(self):
        msg="• "

        if(self.numero==" "):
            msg="No digito ningun numero"
            return msg
        
        if(self.numero>0):
            msg+="El numero es mayor a cero"
        elif(self.numero<0):
            msg+="El numero es menor a cero"
        else:
            msg+="El numero es igual a cero (es neutro)"
        

        if(self.numero%2==0):
            msg+=" y es par"
        else:
            msg+=" y es impar"

        return msg