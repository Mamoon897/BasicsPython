def sum_numbers(n):
    sum_result = 0
    i = 1
    while i <= n:
        sum_result += i
        i += 1
    return sum_result

num = int(input("Enter a positive integer: "))
print("The sum of numbers from 1 to", num, "is", sum_numbers(num))
