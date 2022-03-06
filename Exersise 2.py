def makeposive(number):
    new_value = abs(number)
    return new_value



numbers = int(input("Enter a number to change to be positive: "))
print(f"the positive value of {numbers} is {makeposive(numbers)}")
