def calculate_employee_details():
    basic_salary = float(input("Enter basic salary for the employee: "))
    if basic_salary >= 20000:
        hra = basic_salary * 0.2
        da = basic_salary * 0.3
    else:
        hra = basic_salary * 0.1
        da = basic_salary * 0.2
    total_salary = basic_salary + hra + da
    print(f"Total salary: {total_salary}")

calculate_employee_details()