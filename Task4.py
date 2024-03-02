def calculate_sum(number):
    return sum(range(1, number + 1))

number = int(input("Enter a number: "))
sum_of_numbers = calculate_sum(number)
print(f"The sum of all values from 1 to {number} is: {sum_of_numbers}")