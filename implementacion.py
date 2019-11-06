
# Se declara la clase principal que tendrá las funciones iniciales 
# que adquirirán, o modificarán otras clases

class Algoritmo():

  # Se declara una función que hará uso de las demás funciones
  def plantilla(self):
      # Se definen los métodos que se ejecutarán al
      # hacer uso de esta función
      self.paso_1()
      self.paso_2()
      self.paso_3()

  # Se inicializan las tres funciones que llama la función plantilla
  # con sus respectivas acciones según sea el caso
  def paso_1(self):
      print('Se encuentra en la primera definición de la función paso 1')
      pass

  def paso_2(self):
      print('Se encuentra en la primera definición de la función paso 2')
      pass

  def paso_3(self):
      print('Se encuentra en la primera definición de la función paso 3')


# Se declaran las otras clases que adquieren y/o sobreescriben las funciones
# de la clase Algoritmo. Todas aquellas funciones que no se sobreescriban
# se mantienen igual para la clase.


# La clase AlgoritmoA modifica la función paso_1() y paso_2(), 
# mientras que la clase paso_3() se mantiene igual
class AlgoritmoA(Algoritmo):

  def paso_1(self):
      print('Se sobreescribió la funcion paso 1 inicial en el Algoritmo A')

  def paso_2(self):
      print('Se sobreescribió la funcion paso 2 inicial en el Algoritmo A')


# La clase AlgoritmoB modifica la función paso_1() y paso_3(), 
# mientras que la clase paso_2() se mantiene igual
class AlgoritmoB(Algoritmo):

  def paso_1(self):
      print('Se sobreescribió la funcion paso 1 inicial en el Algoritmo B')

  def paso_3(self):
      pass


# Finalmente, la clase AlgoritmoC modifica la función paso_3(),
# mientras que las demás funciones se mantienen igual
class AlgoritmoC(Algoritmo):

  def paso_3(self):
      print('Se sobreescribió la funcion paso 3 inicial en el Algoritmo C')


# Se imprimen los resultados de cada una de las funciones para cada clase

print ('Algoritmo A: \n')
a = AlgoritmoA()
a.plantilla()

print ('\n\nAlgoritmo B:\n')
b = AlgoritmoB()
b.plantilla()

print ('\n\nAlgoritmo C:\n')
c = AlgoritmoC()
c.plantilla()

# Esto nos permite cambiar las funciones que utilizará cada clase según
# se necesite, pues se puede dar el caso en que una clase necesite una
# función tal cual como se encuentra en la clase principal, pero la misma 
# clase necesita cambiar otra función para cumplir su objetivo.