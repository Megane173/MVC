from modelo_numero import Numero
from vista_formulario import Vista
from controlador import Controlador

#Codigo principal

obj_vista=Vista()
obj_modelo=Numero()
obj_controlador=Controlador(obj_modelo, obj_vista)

obj_controlador.mostrar_menu()

"""""
#Paso 5
obj_numero=Numero()
obj_numero.set_numero(5)
print(f"El numero es: {obj_numero.get_numero()}")

#Paso 6
print("Ahora evalua....")
print(obj_numero.validar_numero())

#prueba vista
obj_vista=Vista()

dato_numero=obj_vista.hacer_campo()
print(dato_numero)

"""""
