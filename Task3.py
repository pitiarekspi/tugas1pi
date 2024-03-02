def classify_number(number):
    if number < 100:
        return "Small"
    elif number > 200:
        return "Large"
    else:
        return "Medium"

number = int(input("Enter a number: "))
classification = classify_number(number)
print(f"The number {number} is: {classification}")