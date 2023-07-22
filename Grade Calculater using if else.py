def grade_calculator(score):
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade

score = float(input("Enter the numeric score: "))
print("Your grade is:", grade_calculator(score))
