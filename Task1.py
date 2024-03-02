def calculate_monthly_salary(salary):
    monthly_salary = round(salary / 12)
    return monthly_salary

salary = int(input("Enter your salary: "))
monthly_salary = calculate_monthly_salary(salary)
print(f"Your monthly salary is: {monthly_salary}")