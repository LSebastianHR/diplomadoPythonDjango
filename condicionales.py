cond_1 = False or 2>=8
cond_2 = True


if (cond_1 and cond_2) or cond_2:
  print('es verdad')
    else:
  print('no es verdad')


#--------------


  if (condicion_1 and condicion_2) or condicion_2:
  print('es verdad')
  elif condicion_1:
  print('solo se cumple la condicion 1')
    else:
  print('ninguna fue verdad es verdad')

#--------------------------

  edad = int(input("¿Cuántos años tiene? "))
gen = int(input("¿cual es su genero? | 1=femenina | 2 = Masculino |"))

if edad < 18:
    print("Es usted menor de edad")
else:
  if gen == 1:
    print("Es usted mayor de edad")
    print("¡Bienvenida!")

if gen == 2:
   print("Es usted mayor de edad")
   print("¡Bienvenido!")