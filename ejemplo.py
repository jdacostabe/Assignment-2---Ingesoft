class Calculadora():

  def calcular(self, lista):
    if sum(lista)>0:
      self.case_1()
    elif sum(lista)==0:
      self.case_2()
    else:
      self.case_3()

  def case_1(self):
    pass

  def case_2(self):
    pass

  def case_3(self):
    pass




class Calculadora_01(Calculadora):
  def case_1(self):
      print("Gano Plata Perro")

  def case_2(self):
      print("No hubiera hecho nada")

  def case_3(self):
      print("Buena :v Pelotudo")



a = Calculadora_01()
a.calcular([41,2,3])