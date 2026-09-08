#Hypotenuse of a triangle
#Camia - Luoang

import math #imports advanced math libraries for more compact code

print("Hello! Welcome to the Hypotenuse Finder for a right triangle!") #welcomes user

a = float(input("Enter the length of side A: \n")) #inputting the length of both sides
b = float(input("Enter the length of side B: \n")) #float converter for arithmetic and decimal values

hypotenuse_length = math.sqrt(math.pow(a, 2) + math.pow(b, 2)) #calculating the hypotenuse length

print(f"The length of the hypotenuse is {hypotenuse_length:.2f} (to 2 decimal places). Bye!") #f-string to make the output line more readable, :.2f to show the number to 2 decimal places