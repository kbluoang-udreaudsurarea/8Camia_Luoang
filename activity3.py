import re

student_id = input("Enter Student ID: ")
valid = True

formaty = r"\d{4}-\d{4}"

if re.fullmatch(formaty, student_id):
    print("Valid Student ID.")
else:
    print("Invalid Student ID.")
    

