asientos=[
[1,2,3,4,5,6],
[7,8,9,10,11,12],
[13,14,15,16,17,18],
[19,20,21,22,23,24],
[25,26,27,28,29,30],
[31,32,33,34,35,36],
[37,38,39,40,41,42]
]
Asiento_normal=78900
Asiento_vip=240000

while True:
    # MENU
    print()
    print("********** Vuelos DUOC **********")
    print()
    print("1.- Ver asientos disponibles")
    print("2.- Comprar asiento")
    print("3.- Anular vuelo")
    print("4.- Modificar datos de pasajero")
    print("5.- Salir")
    opcionMenu=int(input(" Ingrese una opcion:"))

    # SENTENCIAS CONDICIONALES
    if opcionMenu==1:
        for fila in asientos:
            print()
            contadorAsiento=1
            for cadaAsiento in fila:
                print(cadaAsiento,end="\t")
                if contadorAsiento==3:
                     print(end="\t\t")
                contadorAsiento=contadorAsiento+1
            print()

    elif opcionMenu==2:
        print(" comprar asientos")
    elif opcionMenu==3:
        print("Anular vuelo")
    elif opcionMenu==4:
        print(" Modificar datos pasajeros")
    elif opcionMenu==5:
        print(" Salir")
    else:
        print(" Seleccione una opciòn valida ")
    break