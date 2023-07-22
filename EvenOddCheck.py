def odd_even_checker(number):
    if number % 2 == 0:
        result = "even"
    else:
        result = "odd"
    return result

num = int(input("Enter a number: "))
print(f"The number {num} is {odd_even_checker(num)}.")