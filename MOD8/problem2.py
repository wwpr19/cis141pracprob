#2. Write a Python program that allows users to log their hiking trips. The program
should:
- Use a while loop to repeatedly ask for a hike name and distance in miles
- Save each entry to hiking_log.txt (each hike on a new line)
- When the user presses 0, exit the loop & print the contents of hiking_log.txt


hike = input("Hike Name: ")
miles = int(input("Miles Hiked: "))

file = open("hiking_log.txt","w")

while hike !="0" and miles != "0":
    file.write(hike + ": Miles Hiked - " + str(miles) + "\n")
    hike = input("Hike Name: ")
    miles = int(input("Miles Hiked: "))

file.close()

file = open("hiking_log.txt","r")
content = file.read()
print(content)
file.close()
