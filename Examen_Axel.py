juegos = {
'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True,
'NovaStudio'],
'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False,
'BrightWorks'],
'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True,
'OrionGames'],
'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True,
'VelocityLab'],
'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False,
'GreenSeed'],
'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False,
'IronGate'],
}
inventario = {
'G001': [9990, 7],
'G002': [19990, 0],
'G003': [42990, 3],
'G004': [14990, 5],
'G005': [17990, 9],
'G006': [39990, 2],
}
opt= 0
def leer_opcion():
    while opt == 0:
        try:
            opt= input("ingrese una opcion:")
        except ValueError:
            print("intente una opcion numerica:")
        if opt > 0 and opt < 6:
            print(f"ha seleccionado la opcion {opt}")
        else:
            print("opcion fuera del rango")

def buscar_codigo():
    for buscar in juegos:
        print("el codigo es: ", buscar)

def stock_plataforma():
    plataforma= input("ingrese la plataforma deseada: ").upper
    for i in juegos():
        if plataforma == juegos:
            print(inventario[buscar_codigo("stock")])
        


def buscar_precio(p_min,p_max):
    try:
        p_min = input("ingrese el precio minimo")
    except ValueError:
        print("ingrese numeros enteros: ") 
    try:
        p_max = input("ingrese el precio maximo")
    except ValueError:
        print("ingrese numeros enteros: ") 
    if p_min > p_max and p_min < 0 and p_max < 0:
        print("el precio minimo no puede ser mayor al precio maximo")
    else:
        print("el rango de busqueda esta correcto: ")
def actualizar_precio():
    
def agregar_juego():

def eliminar_juego():

def menu_principal(menu):
    while opt != 6:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Stock por plataforma")
        print("2. Búsqueda de juegos por rango de precio")
        print("3. Actualizar precio de juego")
        print("4. Agregar juego")
        print("5. Eliminar juego")
        print("6. Salir")
        print("=====================================")

        if opt== 1:
            stock_plataforma()
        elif opt == 2:
            buscar_precio()
        elif opt == 3:
            actualizar_precio
        elif opt == 4:
            agregar_juego
        elif opt == 5:
            print(buscar_codigo())
        elif opt == 6:
            print("salio del programa")
    return(menu)