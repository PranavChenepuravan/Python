# -*- coding: utf-8 -*-
"""ListToList.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tXSxpxEDriVVg5s_YouDXIQStvNmovxF
"""

list_fruit=["Apple","Orenge","Mango","Kiwi"]
list_new=[]
for f in list_fruit:
  if 'a' in f:
    list_new.append(f)
  elif 'A' in f:
    list_new.append(f)
  else:
    print("")
print(list_new)