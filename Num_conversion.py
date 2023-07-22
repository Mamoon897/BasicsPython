import os
def clear():
    os.system('cls')

clear()
a= input("insert a number for conversion ") # Binary Conversion 
                                            # Its base is 2
                                            # 0b is used as suffix for binary number
a=int(a)
print("binary form of this number is           :",bin(a))

print("Ocatal form of this number is           :",oct(a))  # 0o is used as suffix for identification

print("Heaxadecimel form of this number is     :",hex(a))  # 0x is used as suffix 


input()