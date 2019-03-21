def Menu():
    print ("Calculadora")
    print ("Menu")
    print ("1) Suma")
    print ("2) Resta")
    print ("3) Multiplicacion")
    print ("4) Division")
    print ("5) Exponencial")
def Calculadora():
    """Funcion Para Calcular Operaciones Aritmeticas"""
    Menu()
    opc = int(input("Selecione Opcion\n"))
    while (opc >0 and opc <6):
        x = float(input("Ingrese Numero\n"))
        y = float(input("Ingrese Otro Numero\n"))
        dicc = {"suma":x+y,"resta":x-y,"multiplicacion":x*y,"division":x/y,"exponencial":x**y}
        if (opc==1):
            print ("La Suma es:", dicc["suma"])
            opc = int(input("Selecione Opcion\n"))
        elif(opc==2):
            print ("La Resta es:",dicc["resta"])
            opc = int(input("Selecione Opcion\n"))
        elif(opc==3):
            print ("La Multiplicacion es:",dicc["multiplicacion"])
            opc = int(input("Selecione Opcion\n"))
        elif(opc==4):
            try:
              print ("La Division es:", dicc["division"])
              opc = int(input("Selecione Opcion\n"))
            except ZeroDivisionError:
              print ("No se Permite la Division Entre 0")
              opc = int(input("Selecione Opcion\n"))
        elif(opc==5):
            print ("El Exponencial es:",dicc["exponencial"])
            opc = int(input("Selecione Opcion\n"))

Calculadora()
print ("Por favor seleccione del 1 al 5")