#Marc Gonzalez
#7/10/14
#selection exercise 2.3

hours = int(input("please enter the amount of hours you have worked this week: "))
pay_rate = int(input("Please enter the hourly rate of your job: "))

if hours >40 :
    if hours >60:
        print("You are working over legal limit")
    else:
        overtime = hours - 40
        overtime_pay = pay_rate *1.5
        overtime_total = overtime * overtime_pay
        weekly_pay = 40 * pay_rate
        income = overtime_total + weekly_pay
        print(income)

else:
    income= hours * pay_rate
    print(income)


