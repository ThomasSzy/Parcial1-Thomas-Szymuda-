#Thomas Szymuda 1D FUNCIONES
#DNI:44256320

import re
import random
import datetime
import json
#-----------------------------------------------#
#1
def traer_datos(path:str)->list:
    """     
    Brief: Normalizamos el archivo csv, quitamos los signos $% y creamos una lista con un diccionarios dentro. y si no hay 
            un archivo csv va a devolver un error y un return con -1
    Parameters:
    with: abre el archivo y crea una lista.
    for personajes: ingresa en el archivo y lee, separa cuando tenemos una "," y cuando tenemos un "|"
                    realizando nuestra lista, luego separamos dandoles una key a cada separacion y lo agregamos a la lista
                    con un append
    return: returnamos la lista a nuestra funcion.
    """
    with open(path,"r",encoding = "utf-8") as archivo:
        lista_personajes = []
        if not path:
            print("ERROR NO HAY PATH")
            return(-1)
        
        for personajes in archivo:
            lectura = re.split(",|\n",personajes)   
            luchadores = {}
            luchadores["id"] = int(lectura[0])
            luchadores["personaje"] = lectura[1].lower()
            luchadores["raza"] = re.split(r"-(?=[H])",lectura[2].lower()) #->los parentesis hace que con el ? no te reemplace la H
            luchadores["poder_de_pelea"] = int(lectura[3].replace(" ",""))
            luchadores["poder_de_ataque"] = int(lectura[4].replace(" ",""))
            luchadores["habilidades"] = re.split(r"\s\|\$\%|\|\$\%",lectura[5].strip().lower())
            lista_personajes.append(luchadores)
    return lista_personajes

def orden_id(path:str)->None:
    for luchadores in traer_datos(path):
        """     
        Brief:En esta funcion realizamos un tabeo \n para que quede visualmente mas comodo.
        Parameters:
        format: lo que realizamos para ordenar los keys y darles su espacio con \n 
        return: no returnamos nada
        """
        print("id: {0}\npersonaje: {1}\nraza: {2}\npoder_de_pelea: {3}\npoder_de_ataque: {4}\nhabilidades:{5}\n ".format(
            luchadores["id"],
            luchadores["personaje"],
            luchadores["raza"],
            luchadores["poder_de_pelea"],
            luchadores["poder_de_ataque"],
            luchadores["habilidades"]
            ))
        print(luchadores["habilidades"])
#-----------------------------------------------#
#2
def separarlos(lista:list,key:str)->None:
    """     
    Brief:Realizamos un diccionario el cual cuente las cualquier tipo de str que le agreguemos a la funcion y devuelve un diccionario
            con las veces que aparece en la lista.
    Parameters:
    diccionario: guarda los nombres que hay en cada key y cuenta cuantos hay dentro de cada una.
    for: lo buscamos en la lista los luchadores y los vamos contado por su respectiva key
    2do for:recorre mediante una variable nueva el tipo de lista  tipo_carateristica_key
    if:Lo que realiza es ver si la variable tipo conteos este creada dentro del diccionario de no estar, la crea
    tipo_conteo = Si el tipo de tipo_conteo no es una lista, se crea una lista que contiene el valor tipo_conteo.
    2do for:lo que realiza es printear de manera ordenada la cantidad de personajes que pertenecen a el tipo de key que le damos.
    """
    conteo_tipos = {}
    for luchadores in lista:
        tipo_carateristica_key = luchadores[key]
        for tipo_conteo in tipo_carateristica_key:
            if tipo_conteo in conteo_tipos:
                conteo_tipos[tipo_conteo] +=1
            else:
                conteo_tipos[tipo_conteo] = 1
    for tipo_caracteristica, cantidad_tipo, in conteo_tipos.items():
        print(f"Hay {cantidad_tipo} personajes con {key} - {tipo_caracteristica}")
#-----------------------------------------------#
#3
def raza_tipo(lista: list)->None:
    """     
    Brief:Almacena los nombres de los que tienen ese tipo de raza y luego los printeamos ordenadamente.
    Parameters:
    diccionario: Este diccionario guarda los nombres de los personajes que pertenecen a esa raza, y su poder de ataque
    for: Buscamoslos luchadores y los vamos ordenando por su raza dentro de la lista
    primer print: El primer print nos va a dar la raza y va a guardar el personaje que esta dentro de el diccionario razas
    for: va a tomar el personaje y el poder y lo va a buscar en la el diccionario de razas y los va a ordenar
    .format: ordena nombres, raza y poder de su respectivo personaje
    """
    razas_totales= {}
    for personajes_razas_totales in lista:
        for raza in personajes_razas_totales["raza"]:
            if raza in razas_totales:
                razas_totales[raza].append((personajes_razas_totales["personaje"], personajes_razas_totales["poder_de_ataque"]))
            else:
                razas_totales[raza] = [(personajes_razas_totales["personaje"], personajes_razas_totales["poder_de_ataque"])]
    for raza, personajes in razas_totales.items():
        print("\nLos Personajes de raza /{0}\ son:".format(raza))
        for personaje, poder in personajes:
            print("Nombre: {0} || Poder de Ataque: {1}".format(personaje, poder))
#-----------------------------------------------#
#4 
def lista_personaje_habilidad(lista:list)->None:
    """     
        Brief:Realizamos la busqueda de la habilidad en la lista y tomamos las habilidades .
        Parameters:suma,promedio y return
        for:
        promedio:Saca el promedio entre ambas
        return:Devuelve el promedio listo.
    """
    ingreso_de_habilidad = dato_ingresado(lista,"habilidades")
    for habilidad in lista:
        if ingreso_de_habilidad in habilidad['habilidades']:
            promedio = promedios(habilidad["poder_de_pelea"],habilidad["poder_de_ataque"])
            print(f"el personaje con esa habilidad es {habilidad['personaje']} su raza es : {habilidad['raza']} y El promedio es de {promedio}")

def dato_ingresado(lista:list,dato:str)->str:
    """     
        Brief:Ingresamos la lista con un len y si la lista es indistinta a 0 es que se valido bien, y comenzamos a pedir los datos
        Parameters:
        while y for:Lo que realizamos en el primer while es igualar la bandera sea la flag_primera o flag_valido y que el usuario 
        ingrese un dato, nosotros ese dato lo vamos a enviar a recorrer la lista y con la key.
        for: buscamos en la lista e igualamos el ingreso del usuario con la key que colocamos y valida si es correcto o no.
        return:El return nos devuelve el dato correcto y lo evaluamos en la otra funcion
    """
    if  len(lista) != 0:
        flag_valido = True
        flag_primera = True

        while flag_primera == True or flag_valido == True:
            if flag_primera == True:
                flag_primera = False
                ingreso_de_dato_pedido = input("Ingrese la busqueda que nececita: ").lower()
            else:
                ingreso_de_dato_pedido = input("No exixte ese personaje. Vuelve a ingresar: ").lower()
            for luchadores in lista:
                if ingreso_de_dato_pedido in luchadores[dato]:
                    flag_valido = False
        return ingreso_de_dato_pedido

def promedios(primer_dato:float,segundo_dato:float)->int:
    """     
        Brief:Realizamos la suma entre ambos datos y luego lo promediamos entre dos
        Parameters:suma,promedio y return
        suma:Hace la suma entre los dos datos
        promedio:Saca el promedio entre ambas
        return:Devuelve el promedio listo.
    """
    suma = primer_dato + segundo_dato
    promedios = suma / 2
    return promedios
#-----------------------------------------------#
#5
def jugar_batallas(lista:list)->None:
    """     
        Brief:Comienza el juego imprimiendo nombre a elegir y agregandole la funcion de batalla.
        Parameters:for,funcion
        for: printea una lista de personajes para que el usuario le resulte mas facil de elegir
        batalla_personaje: recibe una lista y retorna la batalla y su archivo txt
    """
    for luchadores in lista:
        print(f"{luchadores['personaje']}")
    batalla_personajes(lista)

def personaje_random(lista:list)->tuple:
    """     
        Brief:Generamos un numero random y lo iguala con el id obteniendo nombre y fuerza
        Parameters:funcion,for,if
        numero_random:importamos biblioteca random, que genera un numero aleatorio con ".randint" 
        for: busca en la lista los personajes numero random y lo compara con el id
            luego tomamos el nombre y el poder del personaje
        return: retornamos el poder y el nombre del bot
    """
    numero_aleatorio = numero_random(1,len(lista_personajes))
    for luchadores in lista:
        if numero_aleatorio == luchadores["id"]:
            personaje_maquina = luchadores["personaje"]
            poder_maquina = luchadores["poder_de_ataque"]
    return poder_maquina,personaje_maquina

def numero_random(numero1:int,numero2:int)->int:
    """     
        Brief: generamos un numero aleatorio entre el 1 y el numero final de la lista
        bibilioteca: importamos la biblioteca random
        numero_aleatorio: Genera el numero con .randint
        retur: retornamos un numero random entedeo.
        
    """
    numero_aleatorio = random.randint(numero1,numero2)
    return numero_aleatorio

def personaje_jugador(lista:list)->tuple:
    """     
        Brief:El usuario ingresa un personaje, lo validamos y tomamos el nombre y el poder
        peronaje_usuario:para inicializarlo lo igualamos a un = None
        for:busca en la lista el nonbre y el poder y lo guardamos
        return: retornamos nombre y poder.
    """
    ingreso_de_dato_pedido = dato_ingresado(lista, "personaje")
    
    personaje_usuario_poder = None #->Para inicializarlo
    
    for personaje in lista:
        if ingreso_de_dato_pedido == personaje["personaje"]:
            personaje_usuario_poder = personaje["poder_de_ataque"]
    return personaje_usuario_poder,ingreso_de_dato_pedido

def batalla_personajes(lista:list):
    """     
        Brief:se comparan los poderes del bot y el personaje del usuario y gana el que mas poder tenga
            en caso de empatar estaran ambos nombres y dira empate, y se envia al archivo.txt con
            la hora y la fecha
        Parameters:return,if,elif,else
        traemos dos returns y los igualamos a sus funciones.
        if:comparamos si el personaje del usuario es mas fuerte que el bot
            Si lo es gana el usuario
        elif: Comparamos si el bot es mas fuerte que el usuario si lo es
            Gana el bot
        else:En caso de tener mismo poder de ataque empataran.

    """
    personaje_usuario_poder,ingreso_de_dato_pedido = personaje_jugador(lista)
    poder_maquina,personaje_maquina = personaje_random(lista)
    
    if personaje_usuario_poder > poder_maquina:
        gana = f"El personaje ganador es del Usuario: {ingreso_de_dato_pedido} y el perdedor es {personaje_maquina}"
    elif poder_maquina > personaje_usuario_poder:
        gana= f"El personaje ganador es del Bot {personaje_maquina} y el perdedor es {ingreso_de_dato_pedido}"
    else:
        gana =f"Fue |Empate| {personaje_maquina} Tiene el mismo poder que {ingreso_de_dato_pedido}"
    fecha_hora_batalla = datetime.datetime.now()
    with open("archivo.txt", "a",encoding = "utf-8") as archivo:
        archivo.write(f"La fecha  y hora de la batalla fue {fecha_hora_batalla} y {gana}\n")
#-----------------------------------------------#
#6
def ingreso_nuevo_personaje(lista:list):
        print("!Ingrese   --   Raza!")
        ingreso_de_dato_pedido = dato_ingresado(lista,"raza")
        print("!Ingrese   --   habilidad")
        ingreso_de_dato_pedido = dato_ingresado(lista, "habilidades")

        print(ingreso_de_dato_pedido)
        personajes_varios_criterios(lista)

def personajes_varios_criterios(lista:list):
    pass

#-----------------------------------------------#
#menu
def imprimir_menu(menu:list)->None:
    """     
    Brief:realizamos un menu con varios submenus
    Parameters:
    opcion:Creamos una opcion de la cual se printee y el usuario decida cual utilizar
    """
    for opcion in menu:
            print(opcion)
menu = ["1.Mostrar la datos del archivo","2.Mostrar las cantidad por raza",
            "3.Lista de personajes por raza y sus especificaciones",
            "4.Ingrese habilidad y mostramos personajes que tengan esas habilidades",
            "5.Jugar Batalla","6.Salir"]

lista_personajes = traer_datos("DBZ.csv")

def dragon_ball_app(path:str)->None:
    """     
    Brief:realizamos una app que printee el menu con sus opciones a realizar
    Parameters:
    while: Cuando tenemos True nos imprime la lista
    match: nos da las opciones a elegir
    """
    """ respuesta = funcion_aparte(menu) """
    while True:
        imprimir_menu(menu)
        respuesta=int(input("Ingrese una opcion:    "))
        match respuesta:
            case 1:
                    orden_id("DBZ.csv")
            case 2:
                separarlos(lista_personajes,"raza")
            case 3:
                raza_tipo(lista_personajes)
            case 4:
                lista_personaje_habilidad(lista_personajes)
            case 5:
                jugar_batallas(lista_personajes)
            case 6:
                ingreso_nuevo_personaje(lista_personajes)
dragon_ball_app("DBZ.csv")