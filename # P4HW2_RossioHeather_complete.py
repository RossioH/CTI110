# P3HW2
# 03/27/25
# Heather Rossio
# Hours worked - make loop homework

total_reg_pay = 0
total_overtime_pay = 0
total_gross_pay= 0
total_employees = 0




employee_name = input("Enter employee's name or 'Done' to terminate: ")

while employee_name.lower() != "done":
  hours_worked = float(input("Enter hours worked: "))
  pay_rate = float(input("Enter employee's pay rate: "))

  if hours_worked > 40:
    regular_hours = 40
    overtime_hours = hours_worked - 40 

  else:
    regular_hours = hours_worked
    overtime_hours = 0

  regular_pay = regular_hours * pay_rate
  overtime_pay = overtime_hours * (pay_rate * 1.5)
  gross_pay = regular_pay + overtime_pay   

  total_employees += 1
  total_reg_pay += regular_pay
  total_overtime_pay += overtime_pay
  total_gross_pay += gross_pay

  print("--------------------------------------------------------------------------------")
  print("Employee name:",  (employee_name))

  print(f"{'Hours Worked':<15} {'Pay Rate':<15} {'OverTime':<15} {'Overtime Pay':<15} {'Regular Pay':<15} {'Gross Pay':<15}")
  print("---------------------------------------------------------------------------------")
  print(f"{hours_worked:<15}{pay_rate:<15}{overtime_hours:<15}${overtime_pay:<15.2f}${regular_pay:<15.2f}${gross_pay:.2f}")
    # else statment ends here
  employee_name = input("Enter employee's name or 'Done' to terminate: ")
# Loop breaks here

print()
print(f"Total Employees: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount for regular hours: ${total_reg_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")



