from pen import Pen

def pick_a_color():
  print("""
  1 - black 
  2 - blue
  3 - red
  """)
  user_input = int(input("Pick your color: "))

  if user_input == 1:
    write("black")
  elif user_input == 2:
    write("blue")
  elif user_input == 3:
    write("red")
  else:
    print("BURRO")
    pick_a_color()

def write(color):
  pen = Pen(color)
  print(f"The pen has {pen.ink} words left")
  pen.write()

color = pick_a_color()