#El siguiente ejemplo evidencia un buen uso del principio Hollywood 

#La cuenta de un usuario en un banco tiene una serie de transacciones, estas pueden
#llevar a 3 estados que son deuda, neto y ganancia. El Banco X, posee un algoritmo 
#para calcular el estado de la cuenta. Cada surcusal del banco controla a su manera los 
#estados de la cuenta. 

#Inicialmente en casos de error el algoritmo del banco arrojaba una excepcion para que
#la sucursal la controlara a su manera. 
#Pero con el uso del principio de Hollywood, todo es muy claro, existe un algoritmo base, 
#que necesita 3 funciones que se ejecutaran en cada uno de los estados, estas son definidas
#por la sucursal.


#Algotimo base del banco
class Algoritmo_Banco():
  
  #Función que permite calcular el estado de la transaccion
  def calcular_estado(self, transacciones):

    #Estado de ganacia realiza lo que la sucursal indique
    if sum(transacciones)>0: 
      self.estado_ganacia()

    #Estado neto realiza lo que la sucursal indique
    elif sum(transacciones)==0:
      self.estado_neto()

    #Estado de deuda realiza lo que la sucursal indique
    else:
      self.estado_deuda()

  #Procesamiento para estado de ganacia
  def estado_ganacia(self):
    pass

  #Procesamiento para estado neto
  def estado_neto(self):
    pass

  #Procesamiento para estado de perdida
  def estado_deuda(self):
    pass



#Definicion de una sucursal
class Algoritmo_Sucursal_01(Algoritmo_Banco):

  #Procesamiento para estado de ganacia
  def estado_ganacia(self):
      print("El saldo de tu cuenta es positivo")
      print("Tus ganacias seran consignadas en una cuenta de ahorros")

  #Procesamiento para estado neto
  def estado_neto(self):
      print("Tu saldo es 0, gracias por usar nuestros servicios")
      
  #Procesamiento para estado de perdida
  def estado_deuda(self):
      print("El sado de tu cuenta es negativo")
      print("Debes solicitar un credito a continuacion se te indica como")



#Se define una cuenta corresponete a una sucursal dada
cuenta_01 = Algoritmo_Sucursal_01()

#El flujo de transacciones
transacciones = [12000, -23000, -32000, 70000]

#El proceso de calular el estado
cuenta_01.calcular_estado(transacciones)