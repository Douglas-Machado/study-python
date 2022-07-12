class Computador:
  def __init__(self, brand, ram, gpu):
      self.brand = brand
      self.ram = ram
      self.gpu = gpu
  
  def ligar(self):
    print('turning on')

  def desligar(self):
    print('turning off')

  def infos(self):
    print(self.brand, self.ram, self.gpu)

c_asus = Computador('Asus', '16gb', 'Nvidia')
c_asus.infos()

# c_gigabyte = Computador('Gigabyte', '16gb', 'AMD')
# print(c_gigabyte.brand, c_gigabyte.ram, c_gigabyte.gpu)

