#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to
#it. Write a Python script that reads a file gardening_tips.txt and prints
#out each tip one by one.

file = open("gardening_tips.txt","w")
file.write("tip 1: Read the care information on the plants lable \n")
file.write("tip2: Be consistant with watering them\n")
file.write("Tip3: Water in the morning so the sun dosnt burn your plants\n")
file.close()
