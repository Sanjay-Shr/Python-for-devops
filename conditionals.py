Day_of_week = input ("Enter the day of week").lower()
if Day_of_week == "SATURDAY" or "SUNDAY":
    print("I will learn Devops")
else:
    print("I will practice Devops")


num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second numnber : "))
choice = input ("Enter the operations +, -, *, /, %")
if choice == "+":
    addition = num1 + num2
    print ("The addition is : ",addition)
elif choice == "-":
    subtraction = num1 - num2
    print ("The subtraction is : ", subtraction)
elif choice == "*":
    mult = num1 * num2
    print ("The Mult is : ", mult)
elif choice == "/":
    div = num1 / num2
    print("The Div is : ", div)
elif choice == "%":
    rem = num1 % num2
    print ("The rem is : ", rem)
else:
    print ("Invalid number")