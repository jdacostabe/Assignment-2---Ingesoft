# Se declara la clase principal que tendrá las funciones iniciales 
# que heredarán las demás clases

class Algoritmo():    
  # Se inicializan las funciones que tendrán las clases
  # que hereden algoritmo
  def paso_1(self):
      pass

  def paso_2(self):
      pass




# Se declaran las otras clases que herendan los métodos
# de la clase Algoritmo.

class AlgoritmoA(Algoritmo):
  def paso_1(self):
      print('Este es el paso 1 del algoritmo A')

  def paso_2(self):
      print('Este es el paso 2 del algoritmo A')


class AlgoritmoB(Algoritmo):
  def paso_1(self):
      print('Este es el paso 1 del algoritmo B')

  def paso_2(self):
      print('Este es el paso 2 del algoritmo B')




# Se declara otra clase que llama las funciones de la
# clase que se le indique en el constructor
class selector():
  def _init_(self,nueva_clase):
    self.clase = nueva_clase

  def pasos(self):
    self.clase.paso_1()
    self.clase.paso_2()


# Se crea un objeto de cada una de las clases AlgoritmoA y AlgoritmoB
# dentro de la clase selector, enviando como parámetro al constructor de
# esta última la clase a crear. Según la clase que se indica, las funciones 
# paso_1 y paso_2 son diferentes, por lo tanto la función pasos también lo es. 

print ('Algoritmo A:\n')
a = selector(AlgoritmoA())
a.pasos()

print ('\n\nAlgoritmo B:\n')
b = selector(AlgoritmoB())
b.pasos()

# De esta forma, se puede cambiar el resultado de la función pasos, según la
# clase que se indica en el construtor de la clase selector, la única restricción
# es que la clase que se indique, herede los métodos de la clase Algoritmo.