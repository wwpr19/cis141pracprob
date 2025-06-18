#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated
#by commas. Write a program that reads the poll.txt file
#Count how many votes "yea" or "nay" received and print the results.

count_y = 0
count_n = 0

file = open("poll.txt", "r")
content = file.read().lower().strip()
votes = content.split(",")
file.close()

for vote in votes:
    if vote == "yea":
        count_y += 1
    elif vote == "nay":
        count_n += 1

print(count_y, "yea", count_n, "nay")
if count_y > count_n:
    print("Votes are for")
else:
    print("Votes are against")
