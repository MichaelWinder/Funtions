def Print_name():
    name = input("What is your name: ")
    times = int(input("How many times do you want your name to print: "))
    i = 1
    while i < times:
        print(name)
    i += 1
print(Print_name())
