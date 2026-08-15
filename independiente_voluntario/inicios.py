#import math
#from matplotlib import pyplot as plt

numero_entero = 5
numero_decimal = 9.4
texto = "string"
caracter = 'e'
boleano_valor_de_verdad = True
nada = None

tiempo = 3.42
# condicionales
if tiempo < 5:
    print("rápido")
elif tiempo == 5:
    print("normal")
else:   
    print("lento")
# ciclo for

lista = [1, 2, 3, 4, 5]
for numero in lista:
    print(numero)   

intento = 0
while intento < 5:
    print("intento", intento)
    intento += 1    

try:
    resultado = 10 / 0 
except ZeroDivisionError:
    print("Error: División por cero")

tiempo = 0.005
if tiempo < 0.001:
    categoria = "rapido"
    print("Categoría: rápido")
elif tiempo < 0.01:
    categoria = "moderado"
    print("Categoría: moderado")
else:
    categoria = "lento"
    print("Categoría: lento")
