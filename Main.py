#Biblio campus
    #gestion libros 
        #agregar
        #actualizar 
        #eliminar 
    #prestamo de libros 
        #crear 
    #devolucion de libros 
        #crear 
    #listar libros
    #listar libros prestados 
        #lista solo los libros que no han sido devueltos
    # historial de prestamos 
        #listado 
    #salir 
#realizar en modulos (pendiente)

#libro -> codigo,nombre,autor,editorial.
#prestamo -> fecha.devolucion,nombre,documento 
#historial->[prestamo]

import os

def limpiarConsola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    input("Presione enter para continuar")

def enterParaContinuar(mensaje : str = "Enter para continuar..."):
    input(mensaje)

def validarInput(titulo : str, valMin: int = 0, valMax: int = 5):
    while True:
        try:
            rta = int(input(titulo))
            if rta >= valMin and rta <= valMax:
                return rta
            else:
                print(f"Por favor ingrese solo valores permitidos... \nRango de {valMin} a {valMax}")
                enterParaContinuar()
                limpiarConsola()
        except:
            enterParaContinuar("OIGA ESTA MAL, INTENTALO DE NUEVO")

def libro(codigo : str, nombre:str, autor : str, editorial:str):
    return {"codigo":codigo, "nombre":nombre, "autor": autor, "editorial":editorial}
    pass
def gestionarLibros(titulo :str):
    limpiarConsola()
    while True:
        print(titulo)
        opc = validarInput("Seleccione una opcion: ",valMin=1, valMax=4)
        if opc == 1:
            pass
        elif opc == 2:
            pass
        elif opc == 3:
            pass
        elif opc == 4:
            break
        else:
            enterParaContinuar("Esta mal, vuelvalo a intentar")
        limpiarConsola()

def solicitarDatos(campos:list):
    respuesta = []
    for c in campos:
        if c["type"] == "entero":
            respuesta.append(validarInput(c["titulo"], 1 , 100))

        elif c["type"] == "texto":
            respuesta.append(input(c["titulo"]))
    return respuesta



menu = """
,---.    ,---.    .-''-.  ,---.   .--.  ___    _ 
|    \  /    |  .'_ _   \ |    \  |  |.'   |  | |
|  ,  \/  ,  | / ( ` )   '|  ,  \ |  ||   .'  | |
|  |\_   /|  |. (_ o _)  ||  |\_ \|  |.'  '_  | |
|  _( )_/ |  ||  (_,_)___||  _( )_\  |'   ( \.-.|
| (_ o _) |  |'  \   .---.| (_ o _)  |' (`. _` /|
|  (_,_)  |  | \  `-'    /|  (_,_)\  || (_ (_) _)
|  |      |  |  \       / |  |    |  | \ /  . \ /
'--'      '--'   `'-..-'  '--'    '--'  ``-'`-'' 

1. Gestion Libros 
2. Prestamo De Libros
3. Devolucion De Libros 
4. Listar Libros
5. Listar Libros Prestados 
6. Historial De Prestamos 
7. Salir 


"""
subMenu = """
    MENU - Gestion De Libros
    1. Agregar
    2. Actualizar 
    3. Eliminar 
    4. Salir
"""
biblioteca = {
    "libros":[],
    "prestamos":[],
    "historial":[]
}


while True:
    print(menu)
    opc = validarInput("Seleccione una opcion: \n", valMin=1, valMax=7)
    if opc ==1:
        gestionarLibros(titulo=subMenu)
    elif opc == 7:
        enterParaContinuar("Chaooo")
        break
    else:
        enterParaContinuar("OIGA ESTA MAL, INTENTALO DE NUEVO")
    limpiarConsola()


