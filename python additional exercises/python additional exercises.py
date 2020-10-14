annual_salary = (input("Please enter your annual salary: "))
gross_monthly_salary = ("annual_salary / 12")
print(gross_monthly_salary)

#This is for full time employees and as well as other.
#Full time pays 29.5% and other 25%.

income_tax = float(input("Please enter the amount of income tax you pay without a percentage sign:"))
net_salary = ("gross_monthly_salary - income_tax")
print(net_salary)
