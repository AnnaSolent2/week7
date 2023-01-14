import matplotlib.pyplot as plt

def display(x, y):
  plt.plot(x, y)
  plt.show()

def run():
  print("Running...")
  x_values = [1, 2, 3, 4, 5]
  y_values = [1, 4, 9, 16, 25]
  display(x_values, y_values)

run()

def small():
  x = [3, 3, 4, 4, 3]
  y = [3, 4, 4, 3, 3]
  plt.plot(x, y, 'r:o')
  
def medium():
  x = [2, 2, 5, 5, 2]
  y = [2, 5, 5, 2, 2]
  plt.plot(x, y, 'g--s')
  
def large():
  x = [1, 1, 6, 6, 1]
  y = [1, 6, 6, 1, 1]
  plt.plot(x, y, 'b-p')
  
def run():
  small()
  medium()
  large()
  plt.show()
  
run()

import matplotlib.pyplot as plt

def coordinate():
  print("Please enter an x value:")
  x = int(input())
  
  print("Please enter a y value:")
  y = int(input())
  
  return (x, y)
  
def path():
  print("Retrieving path...")
  x_values = []
  y_values = []
  
  for count in range(4):
    data = coordinate()
    x_values.append(data[0])
    y_values.append(data[1])
    
  return [x_values, y_values]
  
  
def run():
  values = path()
  plt.plot(values[0], values[1], "r--o")
  plt.xlabel("x values")
  plt.ylabel("y values")
  plt.show()
  
run()

import matplotlib.pyplot as plt
import random as rnd

def data():
  paths = {}
  
  print("What type of line (:, -- or -)?")
  line_style = input()
  
  print("What colour (r, g or b)?")
  colour = input()
  
  print("What type of marker (o, s or ^)?")
  marker_style = input()
  
  paths['line_style'] = line_style
  paths['colour'] = colour
  paths['marker_style'] = marker_style
  
  return paths
  
def generate():
  print("How many lines would you like to display?")
  num_lines = int(input())
  
  for num_line in range(num_lines):
    values = data()
    x = rnd.sample(range(1, 10), 5)
    y = rnd.sample(range(1, 10), 5)
    format = f"{values['colour']}{values['line_style']}{values['marker_style']}"
    plt.plot(x, y, format)
  
  plt.show()


def run():
  print("Running...")
  generate()
  print("Done!")
  
run()
