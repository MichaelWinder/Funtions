def check_bmi(bmi):
    if bmi < 18.5:
        return "Underwieght"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overwieght"
    elif bmi < 30:
        return "Obese"
bmi = int(input("What is your Bmi: "))
print(check_bmi(bmi))
