try:
    pin = int(input("Create a 6-digit PIN: "))
    if len(pin) != 6:
        print("Invalid PIN.")
    else:
        print("Valid PIN.")
except ValueError:
    print("Invalid PIN.")
