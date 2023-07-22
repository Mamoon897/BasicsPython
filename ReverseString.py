def reverse_string(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string

text = input("Enter a string: ")
print("Reversed string:", reverse_string(text))
