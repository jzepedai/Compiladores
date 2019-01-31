# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 17:10:37 2019

@author: Julian
"""
#                       Functions definition
def sumar(a,b):
        return a+b
    
def restar(a,b):
        return a-b
    
def multi(a,b):
        return a*b
    
def div(a,b):
        return a/b
    
def pot(a,b):
        return a**b
    
#                       Variables declaration
    
diccionario={"pi": 3.14159265359}

linea = ""


print("Welcome to MathJul")
print("Enter an operation separated by spaces")
print("Example: 3 + 5, radio = 15 ")
print("Enter word clear to exit")
#                       Loop while user doesn't enter the word "clear"

while linea != "clear":
    linea = input()
    if linea == "clear":
        continue
    x = linea.split(" ")
    n  = x[0]
    operador = x[1]
    n3 = x[2]

    if (operador == "+" or operador == "mas"):
        try:
            n = int(n)
        except ValueError:
            n = diccionario.get(n)
        try:
            n3 = int(n3)
        except ValueError:
            n3 = diccionario.get(n3)
        print(sumar(n,n3))
        
    if (operador == "-" or operador == "menos"):
        try:
            n = int(n)
        except ValueError:
            n = diccionario.get(n)
        try:
            n3 = int(n3)
        except ValueError:
            n3 = diccionario.get(n3)
        print(restar(n,n3))
        
    if (operador == "*" or operador == "x"):
        try:
            n = int(n)
        except ValueError:
            n = diccionario.get(n)
        try:
            n3 = int(n3)
        except ValueError:
            n3 = diccionario.get(n3)
        print(multi(n,n3))
        
    if (operador == "/"):
        try:
            n = int(n)
        except ValueError:
            n = diccionario.get(n)
        try:
            n3 = int(n3)
        except ValueError:
            n3 = diccionario.get(n3)
        print(multi(n,n3))

    if (operador == "^" or operador == "**"):
        try:
            n = int(n)
        except ValueError:
            n = diccionario.get(n)
        try:
            n3 = int(n3)
        except ValueError:
            n3 = diccionario.get(n3)
        print(pot(n,n3))

    if (operador == "="):
        diccionario.update({n:int(n3)})
        print("Saved Variable")