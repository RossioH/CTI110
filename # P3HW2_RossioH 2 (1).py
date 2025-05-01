# P3HW2
# 03/15/25
# Heather Rossio
# Hours worked HW

employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))


if hours_worked > 40:
    gross_pay = 40 * pay_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)  
    total_pay = gross_pay + overtime_pay
else:
    total_pay = hours_worked * pay_rate
    overtime_hours = 0
    overtime_pay = 0

print("--------------------------------------------------------------------------------")
print("Employee name:",  (employee_name))

print(f"{'Hours Worked':<15} {'Pay Rate':<15} {'OverTime':<15} {'Overtime Pay':<15} {'Gross Pay':<15}")
print("---------------------------------------------------------------------------------")
print(f"{hours_worked:<15}{pay_rate:<15}{overtime_hours:<15}${overtime_pay:<15.2f}${total_pay:<15.2f}")



    

