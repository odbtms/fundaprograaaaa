import funciones 
contador_vip=0
contador_cancha=0
contador_galeria=0
rut= input("ingrese su rut: ")
while funciones.validar_rut(rut)== False:
    rut=input("ingrese su rut: ")

correo= input("ingrese su correo: ")
while funciones.validar_correo(correo)== False:
    correo=input("ingrese su correo: ")

while True:

    print("1. Vip")
    print("2. galeria")
    print("3. cancha")
    opc= input("opcion: ")

    if opc=="1":
        print("vip")
        contador_vip+=1
    elif opc=="2":
        print("cancha")
        contador_galeria+=1
    elif opc=="3":
        print("galeria")
        contador_cancha+=1
    else:
        print("opc incorrecta")
    
    seguir=input("quiere seguir(si/no): ")
    while seguir!= "si" and seguir != "no":
        seguir=input("quiere seguir(si/no): ")
        
    if seguir=="si":
        continue
    elif seguir== "no":
        break

funciones.boleta(contador_vip,contador_galeria,contador_cancha)

