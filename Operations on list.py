# operations on lists

import os

num1=[99,400,90,103,290]
num=[90,203,40,98,68]
# num=int(num)
# numm1=int(num1)
num.sort()
print(num,":is the sorted form ")
max(num)
print(max(num),":is max in this list")
min(num)
print(min(num),":is min in this list")

print(sum(num),'is sum of list 1\n', sum(num1),'is sum of list 2')
num.extend([48,86,170])
num.pop()
print(num,'this is an extended list')
print(num+num1,'add of two lists')
num2=[num1*num,'multiplication of lists']
print(num2)