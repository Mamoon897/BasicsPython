def bmi_calculator(weight, height):
    # Convert height to meters
    height_meters = height / 100

    # Calculate BMI
    bmi = weight / (height_meters ** 2)

    if bmi < 18.5:
        category = "underweight"
    elif bmi < 24.9:
        category = "normal weight"
    elif bmi < 29.9:
        category = "overweight"
    else:
        category = "obese"
    return bmi, category

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))
bmi, category = bmi_calculator(weight, height)
print(f"Your BMI is {bmi:.2f}, and you are categorized as {category}.")
