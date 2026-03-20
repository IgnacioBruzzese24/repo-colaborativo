# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 16:03:24 2026

@author: nacho
"""

def registrar_habitos():
    """
Permite registrar actividades (hábitos) ingresadas por el usuario.

El usuario puede decidir si desea agregar actividades. En caso afirmativo,
se le solicitará que ingrese el nombre de cada actividad. El proceso se repite
hasta que el usuario indique que no desea agregar más.

La función valida que las respuestas sean 'y' (sí) o 'n' (no).

Returns:
    list: Una lista de strings con las actividades ingresadas por el usuario.
"""
    lista_act=[]
    decision=input("Desea añadir una actividad y/n?: ")
    while not decision=="y" and not decision=="n":
        print("Respuesta no valida, intente nuevamente")
        decision=input("Desea añadir una actividad y/n?: ")
    while decision=="y":
        nueva_actividad=input("Que actividad desea añadir?: ")
        lista_act.append(nueva_actividad)
        decision=input("Desea añadir una actividad y/n?: ")
        while not decision=="y" and not decision=="n":
            print("Respuesta no valida, intente nuevamente")
            decision=input("Desea añadir una actividad y/n?: ")
            
    return lista_act      

def analizar_habitos(lista):
    """
    Analiza una lista de actividades (hábitos) y cuenta cuántas veces aparece cada una.

    Recorre la lista recibida y construye un diccionario donde:
    - las claves son las actividades
    - los valores son la cantidad de veces que aparecen

    Args:
        lista (list): Lista de strings con las actividades registradas.

    Returns:
        dict: Diccionario con el conteo de cada actividad.
    """
    conteo={}
    for actividad in lista:
        if actividad in conteo:
            conteo[actividad]+=1
        else:
            conteo[actividad]=1
    return conteo

