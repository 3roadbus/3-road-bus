from pycat.core import Window
window = Window()
input("Hello, there!   ")
Ans = input('Do you want a cat or a bus?')

if Ans == "cat":
  Cat = window.create_sprite()
  Cat.image = 'cat.jpg'
  Cat.x = 700
  Cat.y = 300
  Cat.scale = 5
  print("This is a cat")
  ACAT = input("Do you want to make the picture bigger?")
  if ACAT == 'true':
    Cat.scale = 7.5
  

window.run()