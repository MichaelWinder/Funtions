def GST_hack():
    exclusive = int(input("What is the price without GST: "))
    total_cost = exclusive * 1.15
    return f"The total cost of your product is ${total_cost:.2f}"


print(GST_hack())
