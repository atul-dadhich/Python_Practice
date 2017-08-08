# Calculates BMR
weight = int(input("Please Enter Your Weight in Kg: \n"))
height = int(input("Please Enter Your Height in Cm: \n"))
age = int(input("Please Enter Your Age in Years: \n"))
gender = input("Are You A Male")

if gender == "y":
    isMale = True
elif gender == "n":
    isMale = False
else:
    print("Error")
    exit()

    # Only for Men

if isMale:
    print("Calculating For Men")
    bmr = 66.5+(13.75 * weight)+(5 * height)-(6.755 * age)
else:
    print("Calculating For Women")
    bmr = 655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

bmr = round(bmr)
print(bmr)



