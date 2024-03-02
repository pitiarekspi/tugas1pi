def calculate_sum_of_numbers():
    total_sum = 0
    while True:
        number = int(input("Enter a number (-1 to stop): "))
        if number == -1:
            break
        total_sum += number
    return total_sum

total_sum = calculate_sum_of_numbers()
print(f"The sum of all numbers entered is: {total_sum}")