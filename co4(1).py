# -*- coding: utf-8 -*-
"""CO4(1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BjfPMvXDM14keSfOTza16_2eJAOJAkhl
"""

class calc():
  def area(self,l,b):
    ar=l*b
    print("Area = ",ar)
    return(ar)
  def per(self,l,b):
    pr=(l*2)+(b*2)
    print("Perimeter = ",pr)
    print("")
    return(pr)

l=0
b=0  
l=int(input("Enter the length: "))
b=int(input("Enter the bridth: "))
fiar=calc()
ar1=fiar.area(l,b)
fipr=calc()
pr1=fipr.per(l,b)
l=int(input("Enter the length: "))
b=int(input("Enter the bridth: "))
sec=calc()
ar2=sec.area(l,b)
sepr=calc()
pr2=sepr.per(l,b)
if(ar1>ar2):
  print("First rectangle have the largets area")
elif(ar2>ar1):
  print("Second rectangle have the largest area")
else:
  print("Boath rectangles have the same area")