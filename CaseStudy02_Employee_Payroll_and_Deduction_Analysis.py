basic_pay = float(input("Enter basic pay (Rs.): "))
overtime_hours = float(input("Enter overtime hours: "))

if basic_pay < 0 or overtime_hours < 0:
    print("Invalid input: values cannot be negative.")
else:
    hra = basic_pay * 0.20
    other_allowance = basic_pay * 0.10
    overtime_pay = overtime_hours * 150
    gross_salary = basic_pay + hra + other_allowance + overtime_pay
    deduction = gross_salary * 0.08
    net_salary = gross_salary - deduction

    print("\n--- Salary Statement ---")
    print("Basic pay: Rs.", round(basic_pay, 2))
    print("HRA: Rs.", round(hra, 2))
    print("Other allowance: Rs.", round(other_allowance, 2))
    print("Overtime pay: Rs.", round(overtime_pay, 2))
    print("Gross salary: Rs.", round(gross_salary, 2))
    print("Deduction: Rs.", round(deduction, 2))
    print("Net salary: Rs.", round(net_salary, 2))
