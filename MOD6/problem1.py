
#1. Create a list of integers (you get to pick!).
#Write code to iterate through the list and calculate the
#sum of all even numbers. Print the resulting sum.

list = [4,94,24,456,7,8,78,45]
sum = 0
for i in list:
    if i % 2 == 0:
       sum +=i      
print(sum)
