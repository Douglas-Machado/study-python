from blueprint import Blueprint
import re

class Pen(Blueprint):
  def __init__(self, color):
    super().__init__(color)
    self.is_empty = True
    self.ink = 100
  
  def write(self):
    user_input = input('Write your text: ')
    words_list = re.split("\s", user_input)
    if self.ink < len(words_list):
      return print("The pen has no ink left")
    self.__save_text(user_input)
    self.ink = self.ink - len(words_list)

  def __save_text(self, text):
    f = open("./imports-py/notebook.txt", "a")
    if self.is_empty:
      f.write(f"color ({self.color}) - {text}")
      self.is_empty = False
    else:
      f.write(f"\ncolor ({self.color}) - {text}")

  def read_text(self):
    f = open("./imports-py/notebook.txt", "r")
    print(f.read())

