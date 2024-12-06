from pycat.core import Window
windows= Window()
bus= windows.create_sprite()
bus.image= 'tnbuso13.jpg'
Customtf= input("Do you want to custom the bus?")
if Customtf == "true" or "yes":
 customX= 'float'
 customX= input("What do you want for the picture's X?")
bus.x= customX
customY= input("What do you want for the picture's Y?")
bus.y= customY
customsize=input("What do you want for the picture's size?")
bus.scale= customsize

print('Detail: X= ',bus.x , 'Y= ', bus.y)
windows.run()