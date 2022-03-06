def uppercase_words():
    name = input("What is your name: ")
    case = int(input("How many letters in your name do you want to be uppercase: "))
    return name[0:case].upper() + name[case:]
print(uppercase_words())
