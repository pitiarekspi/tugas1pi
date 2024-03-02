def calculate_third(number):
    third = round(number / 3)
    return third

number = int(input("Enter a number: "))
third = calculate_third(number)
print(f"The third of {number} is: {third}")