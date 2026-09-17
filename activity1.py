payment_methods = ["Cash", "GCash", "Card"]


method = input("Enter payment method: ")

if method in payment_methods:
    print("Valid payment method.")
else:
    print("Invalid payment method.")
