def overdue_book():
    days = int(input("Enter days overdue: "))
    cost = days * 0.8 + 0.5
    the = 30
    if cost > 30:
        cost = 30
    return f"The fine is ${cost:.2f}"


print(overdue_book())
