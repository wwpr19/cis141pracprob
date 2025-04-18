# 1. Create a program that prints the following output to the screen: 
#"Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."
print("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.")

# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division
#of the first number by the second number.
First = int(input("Please enter a number"))
Second = int(input("Please enter a number"))
print (First + Second, First - Second, First * Second, First / Second)

# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. 
#(https://en.wikipedia.org/wiki/Heron%27s_formula)
import math 
a = float(input("First side of the triangle"))
b = float(input("Second side of the triangle"))
c = float(input("Third side of the triangle"))
semi = float(.5 * (a+b+c))
#print(semi)
Area = math.sqrt( (semi) * (semi-a) * (semi - b) * (semi - c) )
print ("The area of your triangle is", Area)

# 4. Create a program that prompts the user for their birth year and displays a message that says "You are ___ old".
#Use an f-string in your solution to this problem.
BY = int(input("What is your birth year?"))
CY = 2025
print(f" You are { CY-BY } old ")
