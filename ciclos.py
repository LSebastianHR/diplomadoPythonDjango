# Se define una lista de items
# Se realiza una impresion con cada uno de los items de la lista
my_list = ['jasmin', 'edgar', 'yurley', 'fabian']
print(len(my_list))

for i in my_list:
  print('hola ' + i + ', que tengas un buen dia!')

break


for i in range(len(my_list)):
  print(i)
  #print('hola ' + my_list[i] + ', que tengas un buen dia!')

for i in range(10):
  print(i)

break


#Ejecricio
#definir un diccionario con la lista de precios de productos de una tienda y su respectivo valor Ejemplo
#magina que debes preparar una deliciosa comida y quiere saber cuanto te cuesta preparalo con el valor de los ingredientes.
#define una lista y calucula el valot total a pagar por esa comida.


# Definir Diccionario de productos

productos_del_super = {'arroz':1600,'tomate':500,'cebolla':800,'carne':9500,'papa':450,'limon':900,'azucar':1200,'aceite':5600,'mayonesa':1600,'platano':1550,}
productos_del_super

# Lista de productos

lista_almuerzo = {'carne','papa','mayonesa','tomate','cebolla','limon','azucar'}
Valor_almuerzo = 0

# Ciclo de pago

for key, value in productos_del_super.items():
      if key in lista_almuerzo:
          Valor_almuerzo = Valor_almuerzo + value
          print(key,  value)
print("el total a pagar es de: $"+ str(Valor_almuerzo))