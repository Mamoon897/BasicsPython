import os
def clear():
    os.system('cls')

clear()

lst=[]
n =int(input("Enter number of elements in list : "))
  
# iterating till the range 
for i in range(0, n): 
    print("enter the element")
    ele = input()
  
    lst.append(ele) # adding the element 
      
print(lst) 