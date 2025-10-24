


class Numero:

    def __init__(self, numero=" "):
        self.numero=numero

    def get_numero(self):
        return self.numero
    
    def set_numero(self, numero):
        self.numero=numero


    def es_par(self):
        msg="• "

        if(self.numero==" "):
            msg="No digito ningun numero"
            return msg       

        if(self.numero%2==0):
            msg+="Es par"
        else:
            msg+="Es impar"

        return msg
    
    def es_positivo(self):
        msg="• "

        if(self.numero==" "):
            msg="No digito ningun numero"
            return msg
        
        if(self.numero>0):
            msg+="El numero es positivo"
        elif(self.numero<0):
            msg+="El numero es negativo"
        else:
            msg+="El numero es igual a cero (es neutro)"
        
        return msg
