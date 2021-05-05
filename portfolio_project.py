data = int(input("enter the date(just the date)\n"))
name=input("Enter your name\n")
def Cancer(data,name):
  print("Dear",name,"Being in cancer wont let you live a life of a hero today. So prefer being a joker today.This is for",data)
def Taurus(data,name):
  print("Dear",name,"Being in taurus wont let you live a life of a nerd today. So prefer being a extrovert and fun up the whole place today.This is for",data)
def Leo(data,name):
  print("Dear",name,"Being in Leo wont let you live a life of a horse today. So prefer being a tortoise and enjoy the pleasures of being slow today.This is for",data)
if data >=1 and data<=10:
  Cancer(data,name)
elif data >=11 and data<=20:
  Taurus(data,name)
elif data>=21 and data <=31:
  Leo(data,name)
else:
  print("Sorry mate, wrong date!")
