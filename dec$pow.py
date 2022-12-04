#Decimal & POWER CALCULATOR
#HEADINGS........

print("DECIMAL  & POWER CALCULATOR \n")

#THE PROGRAM

print("select any of the two operations \n")
print("DECIMAL CALCULATOR \n")
print("POWER CALCULATOR \n")
Dec_Cal = "WELCOME TO DECIMAL CALCULATOR"
Pow_Cal = "WELCOME TO POWER CALCULATOR"
user = input("Your OPTION below \n")
if user == "DECIMAL CALCULATOR":
    print(Dec_Cal)
    print("Just input any number below to round it off")
    try:
        yournum = float(input("input your decimal below: \n"))
    except ValueError:
        print("error")
    one_decimal_place = round(yournum, 1)
    two_decimal_place = round(yournum, 2)
    three_decimal_place = round(yournum, 3)
    four_decimal_place = round(yournum, 4)
    print("Okay, we got you ?")
    print("How many decimal place")
    a = "a = one_decimal_place"
    b = "b = two_decimal_place"
    c = "c = three_decimal_place"
    d = "d = four_decimal_place"
    print(a)
    print(b)
    print(c)
    print(d)
    B = input("any of these options here \n")
    if B == "a":
        print(one_decimal_place)
        print("This is your answer")
    elif B == "b":
        print(two_decimal_place)
        print("This is your answer")
    elif B == "c":
        print(three_decimal_place)
        print("This is your answer")
    elif B == "d":
        print(four_decimal_place)
        print("This is your answer")
    else:
        print("Error")
elif user == "POWER CALCULATOR":
    print(Pow_Cal)
    try:
        basenum = float(int(input("input your base number below \n")))
    except ValueError:
        print('Error')
    power = (float(int(input("your power below \n"))))
    answer = pow(basenum, power)
    print(answer)
    print("This is your answer")
else:
    print("Wrong Input")


