# 5. A store charges $5 for shipping on any order under $50. 
#If the order amount is $50 or more, shipping is free. 
#Ask the user for the order total and print the total cost, including shipping.

order = int(input("How much is your order?"))
if order < 50:
    New_Total = order+5
    print("Your total is now " + str(New_Total))
else:
    print("Thank you for placing your order. Your total is",order)
