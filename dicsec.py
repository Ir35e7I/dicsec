def imprimir_encabezado():
    encabezado = """
      ██████  ▒█████   ███▄    █ ▓█████▄  ▄▄▄          ▄▄▄       ███▄    █  ▄▄▄       ██▀███   ██ ▄█▀ ▒█████  
    ▒██    ▒ ▒██▒  ██▒ ██ ▀█   █ ▒██▀ ██▌▒████▄       ▒████▄     ██ ▀█   █ ▒████▄    ▓██ ▒ ██▒ ██▄█▒ ▒██▒  ██▒
    ░ ▓██▄   ▒██░  ██▒▓██  ▀█ ██▒░██   █▌▒██  ▀█▄     ▒██  ▀█▄  ▓██  ▀█ ██▒▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░ ▒██░  ██▒
      ▒   ██▒▒██   ██░▓██▒  ▐▌██▒░▓█▄   ▌░██▄▄▄▄██    ░██▄▄▄▄██ ▓██▒  ▐▌██▒░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄ ▒██   ██░
    ▒██████▒▒░ ████▓▒░▒██░   ▓██░░▒████▓  ▓█   ▓██▒    ▓█   ▓██▒▒██░   ▓██░ ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄░ ████▓▒░
    ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ▒▒▓  ▒  ▒▒   ▓▒█░    ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒░ ▒░▒░▒░ 
    ░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ▒  ▒   ▒   ▒▒ ░     ▒   ▒▒ ░░ ░░   ░ ▒░  ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░  ░ ▒ ▒░ 
    ░  ░  ░  ░ ░ ░ ▒     ░   ░ ░  ░ ░  ░   ░   ▒        ░   ▒      ░   ░ ░   ░   ▒     ░░   ░ ░ ░░ ░ ░ ░ ░ ▒  
          ░      ░ ░           ░    ░          ░  ░         ░  ░         ░       ░  ░   ░     ░  ░       ░ ░  
                                      ░                                                                           
    """
    print(encabezado)

imprimir_encabezado()

import itertools
import datetime
import random

def generar_diccionario():
    ubicacion_listado = input("Ubicación del listado de palabras importantes: ")
    longitud_maxima = int(input("Longitud máxima de las palabras generadas: "))
    nombre_diccionario = input("Nombre del diccionario generado: ")
    agregar_numeros = input("¿Deseas insertar números al principio y/o al final de las palabras generadas? (S/N): ")
    comb_caracteres = input("¿Deseas agregar combinaciones de caracteres especiales? (S/N): ")
    if comb_caracteres.lower() == "s":
        max_caracteres = int(input("¿Cuántos caracteres especiales deseas agregar como máximo? "))
    
    palabras = obtener_palabras(ubicacion_listado)
    combinaciones = generar_combinaciones(palabras, longitud_maxima, agregar_numeros, comb_caracteres, max_caracteres)
    
    generar_archivo(nombre_diccionario, combinaciones)

def obtener_palabras(ubicacion_listado):
    with open(ubicacion_listado, "r") as archivo:
        palabras = archivo.read().splitlines()
    return palabras

def generar_combinaciones(palabras, longitud_maxima, agregar_numeros, comb_caracteres, max_caracteres):
    combinaciones = []
    
    # Combinaciones básicas con una sola palabra
    for palabra in palabras:
        combinaciones.append(palabra)
        combinaciones.append(palabra.lower())
        combinaciones.append(palabra.capitalize())
        combinaciones.append(palabra[::-1])
        combinaciones.append(palabra + "@")
        
        if agregar_numeros.lower() == "s":
            for i in range(10):
                combinaciones.append(palabra + str(i))
                combinaciones.append(str(i) + palabra)
    
    # Combinaciones con varias palabras
    for i in range(2, longitud_maxima + 1):
        for combinacion in itertools.permutations(palabras, i):
            combinaciones.append("".join(combinacion))
            combinaciones.append("".join(combinacion).lower())
            combinaciones.append("".join(combinacion).capitalize())
            combinaciones.append("".join(combinacion)[::-1])
            combinaciones.append("".join(combinacion) + "@")
            
            if agregar_numeros.lower() == "s":
                for j in range(10):
                    combinaciones.append("".join(combinacion) + str(j))
                    combinaciones.append(str(j) + "".join(combinacion))
                    
            if comb_caracteres.lower() == "s":
                caracteres_especiales = "-/:;()$&@“‘!?,.[]{}##%^+=•¥£€><~|\__*;"
                for k in range(1, min(max_caracteres + 1, longitud_maxima - i + 1)):
                    for comb in itertools.combinations(caracteres_especiales, k):
                        combinaciones.append("".join(combinacion) + "".join(comb))
                        combinaciones.append("".join(combinacion).capitalize() + "".join(comb))
                        combinaciones.append("".join(combinacion).lower() + "".join(comb))
                        combinaciones.append("".join(combinacion) + "".join(comb) + "@")
    
    fechas = obtener_fechas()
    for fecha in fechas:
        combinaciones.append(fecha.strftime("%Y"))
        combinaciones.append(fecha.strftime("%m"))
        combinaciones.append(fecha.strftime("%d"))
        combinaciones.append(fecha.strftime("%Y%m"))
        combinaciones.append(fecha.strftime("%Y%d"))
        combinaciones.append(fecha.strftime("%m%d"))
    
    return combinaciones

def obtener_fechas():
    fechas = []
    today = datetime.date.today()
    
    for i in range(10):
        fecha = today - datetime.timedelta(days=i*365)
        fechas.append(fecha)
    
    return fechas

def generar_archivo(nombre_diccionario, combinaciones):
    limite_lineas = 100000
    num_archivos = len(combinaciones) // limite_lineas + 1
    
    for i in range(num_archivos):
        archivo_salida = nombre_diccionario + str(i+1) + ".txt"
        with open(archivo_salida, "w") as archivo:
            inicio = i * limite_lineas
            fin = (i+1) * limite_lineas
            archivo.write('\n'.join(combinaciones[inicio:fin]))

generar_diccionario()
