#------------------------------------
#------Captura Basica de Errores-----
#------------------------------------
def dividir():
    print("----Division de dos numeros----")
    try:
        numero1 = int(input("Primer numero: "))
        numero2 = int(input("Segundo numero: "))
        total = numero1 / numero2
        print(f"Resultado: {total}")

    except ZeroDivisionError: 
        print("No puedes ingresar un numero 0")


dividir()

#-------------------------------------
#---------Captura Multiple------------
#-------------------------------------

def suma():
    print("------Multiples excepciones-------")
    try:
        numero1 = int(input("Primer numero: "))
        numero2 = int(input("Primer numero: "))
        total = numero1 + numero2
        print(f"Resultado: {total}")

    except ZeroDivisionError:
        print("No puedes ingresar un numero 0")
    
    except ValueError:
        print("No puedes ingresar una palabra")

suma()


#-----------------------------------------
#------Excepcion personalizadas-----------
#-----------------------------------------

class EdadInvalidaError(Exception):
    def __init__(self, mensaje="La edad no puede ser menor que 0"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def validar_edad(edad):
    print("------- Validar Edad -----------")
    try:
        if edad < 0:
            raise EdadInvalidaError()
        print(f"Edad válida: {edad}")

    except EdadInvalidaError as e:
        print(f"Error: {e}")

validar_edad(25)   
validar_edad(-5)   



#--------------------------------------
#--Limpieza de recursos con finally----
#--------------------------------------

def multiplicacion():
    print("------Limpieza de recursos con finally")
    try:
        numero1 = int(input("Primer numero: "))
        numero2 = int(input("Segundo numero: "))
        total = numero1 * numero2
        print(f"Total: {total}")
    except ValueError:
        print("El valor no es un numero entero")
    finally:
        print("Cerrando archivo..")

multiplicacion()