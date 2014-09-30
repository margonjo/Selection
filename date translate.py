#Marc Gonzalez
#30/09/14
#selection exercise 3.3

day = int(input("please enter the day number: " ))
month = int(input("Please enter the month number: "))
year = int(input("Pease enter the year number: "))



if month == 1:
    month_1 = January
elif month == 2:
    month_1 = February
elif month == 3:
    month_1 = March
elif month == 4:
    month_1 = April
elif month == 5:
    month_1 = May
elif month == 6:
    month_1 = June
elif month == 7:
    month_1 = July
elif month == 8:
    month_1 = August
elif month == 9:
    month_1 = September
elif month == 10:
    month_1 = October
elif month == 11:
    month_1 = November
elif month == 12:
    month_1 = December
else:
    print("the month you entered is not valid")

if day == 1 or 21 or 31 :
    day_expression = "st"

elif day == 2 or 22 :
    day_expression = "nd"

elif day == 3 or 23 :
    day_expression = "rd"

elif day > 31 :
    print("The day you have entered is not valid")

else:
    day_expression = "th"

if 30 < year < 100 :
    pre_year = 19

elif year > 99:
    print("The year you have entered is not valid")

else:
    pre_year = 20

print(" The date you have entered is {0){1} {3} {4)".format(day,day_expression




    
