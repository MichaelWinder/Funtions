
def FACTOR_CHECK():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number that you want to see if its a factor of the first number: "))
    if num1 % num2 == 0:
        return f"Yes {num2} is a factor of {num1}"
    else:
        return f"No {num2} is not a factor of {num1}"


print(FACTOR_CHECK())
