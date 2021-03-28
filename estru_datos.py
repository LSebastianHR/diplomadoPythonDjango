# "vector" Lista de campo mutables 

Vector1=['0','1','2','3','4'] #Definicion de lista
Vector1[-1]                   #obtener ultimo item de la lista
len(Vector1)                  #obtener numero de items de la lista
Vector1.append('5')           #Agregar item a la lista
Vector1[-1]                   #obtener ultimo item de la lista
Vector1.pop()                 #Eliminar ultimo elemento de la lisa
'2' in Vector1                #Validar si el item/valor esta en la lista (responde un voleano)
Vector1(1:4)                  #obtener rango de items
help list                     #Documentacion de python 

# diccionario de datos en las cuales se puede tener subniveles de diccionarios


diccionario1 ={              #Definir Diccionario
    '1+2': 3,
    '3+4': 7,
    '7+8': 15,
    '15+16' : 31
}

diccionario1.get('1+2')     #Obtener valor de la key solicitada
diccionario1['16+17'] = '33'#Agregar dato ak diccionario
diccionario1.get('1+2') + diccionario1.get('1+2') #iterar elementos 
help dict                                         #Docuemntacion    

# Lista de valores inmutables (valores estaticos)
tupl1 = ("lunes","martes","miercoles","jueves","viernes") #definir tupla
tupl1.count("lunes")                                      #contar cuantas veces existe un elemento


tuplacompuesta = ({'rust': '$ 36.000'}, ['a','b','c','d'], 1,2,3)     # Definir tupla compuesta
tuplacompuesta[0]['rust'] = '$ 18.000 50% off'                        #modificar diccionario en tupla
tuplacompuesta