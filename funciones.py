import config
import random
def codigo_ramdom():
    return random.randint(100000,990000)
def validar_rut(rut):
    if rut =="":
        print("campo obligatorio")
        return False
    else:
        return True

def validar_correo(correo):
    if correo=="":
        print("correo invalido")
        return False
    else:
        return True

def boleta(contadorvip,contadorgaleria,contadorcancha):
    with open("boleta.txt","w") as archivo:
        if contadorvip!=0:
            codigo=codigo_ramdom()
            archivo.write("**************************\n")
            archivo.write(f"codigo: {codigo}\n")
            archivo.write("tipo: VIP\n")
            archivo.write(f"cantidad: {contadorvip}\n")
            archivo.write(f" valor: {config.entradas["vip"]*contadorvip}\n")

        if contadorgaleria !=0:
            codigo=codigo_ramdom()
            archivo.write("**************************\n")
            archivo.write(f"codigo: {codigo}\n")
            archivo.write("tipo: Galeria\n")
            archivo.write(f"cantidad: {contadorgaleria}\n")
            archivo.write(f" valor: {config.entradas["galeria"]*contadorgaleria}\n")

        if contadorcancha!=0:
            codigo=codigo_ramdom()
            archivo.write("**************************\n")
            archivo.write(f"codigo: {codigo}\n")
            archivo.write("tipo: cancha\n")
            archivo.write(f"cantidad: {contadorvip}\n")
            archivo.write(f" valor: {config.entradas["cancha"]*contadorcancha}\n")

        


