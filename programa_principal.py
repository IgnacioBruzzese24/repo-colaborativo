# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 16:03:24 2026

@author: nacho
"""
from funciones_habitos import registrar_habitos, analizar_habitos




lista = registrar_habitos()

resultado = analizar_habitos(lista)

print (' resumen de actividades')
print(resultado)

