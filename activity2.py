payment_methods = ["Cash", "GCash", "Card"]


grade = int(input("Enter payment method: "))

if grade >= 0 and grade <= 100:
    print("Valid grade.")
else:
    print("Invalid grade.")
