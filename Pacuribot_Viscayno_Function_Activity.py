def finding_the_sum():
    if num1 == num2 != num3:
        xyz = (num1 * num2) + num3
        print(f"The result is: {xyz} ")
    elif num2 != num3 == num1:
        xyz = (num2 * num3) + num1
        print(f"The result is: {xyz} ")
    elif num1 == num3 != num2:
        xyz = (num1 * num3) + num2
        print(f"The result is: {xyz} ")
    elif num1 != num2 != num3:
        cxz = num1 + num2 + num3
        print(f"The result is: {cxz} ")
    elif num1 == num2 == num3:
        xyz = num1 * num3 * num2
        print(f"The result is: {xyz} ")
    else:
        print("Invalid input")


num1 = eval(input("Enter your first number:"))
num2 = eval(input("Enter your second number:"))
num3 = eval(input("Enter your third number:"))

finding_the_sum()