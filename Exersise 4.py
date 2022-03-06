def a_checker():
    word = input("Enter a word and ill tell you if it starts with A: ")
    x = list(word)
    A_check = x[0]
    if ("a") == A_check:
        return "Yes it Does"
    else:
        return "No it Doesn't"
print(a_checker())
