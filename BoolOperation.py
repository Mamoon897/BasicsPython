
import os

def clear():
     os.system( 'cls' )

clear()


a=input("insert something in a   ")
a=int(a)
b=input("insert SOMETHING IN B   ")
b=int(b)
c=bool(a>b)  # Bool always gives its answer in true or false
             

if(a|b<0): 
 print("invalid input A & B must be greater than Zero 0")

elif (c==True) :
 print("A is greater ")

elif (c==False):
 print("B is greater ")




