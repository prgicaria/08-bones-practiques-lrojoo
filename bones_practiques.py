#!/usr/bin/env python
'''tasca 8. Divisio utilitzant dividend,quocient i residu
Institut Icària
Programació - 1r Batxillerat - Curs 2023-24
Aquest programa demana que introdueixis dos numeros:
 el dividend i el divisor. a continuacio, realitzem
una divisio entre aquests dos numeros i calculem tant el
 quocient com el residu utilitzant les operacions
 aritmetiques de divisio entera i modul.
'''
__author__ = "Luka Rojo Martinovic"
__email__ = "lrojo@instituticaria.com"
__date__ = "2024/10/17"

# Demanar el dividend i el divisor a l'usuari
dividend = int(input("Introdueix el dividend: "))
divisor = int(input("Introdueix el divisor: "))

# Calcular el quocient i el residu
quocient = dividend // divisor
residu = dividend % divisor

# Mostrar els resultats segons l'exemple
print(f"Divisió: {dividend}/{divisor}")
print(f"Quocient: {quocient}")
print(f"Residu: {residu}")
