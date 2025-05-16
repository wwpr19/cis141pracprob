
#3. Create a list of strings. Write code to create a new
#list that includes only the strings longer than three
#characters. Print the resulting filtered list.

S_list = ["fay", "apple", "ten", "potbelly", "sam"]
newS_list = []
for i in S_list:
    if len(i) > 3:
        newS_list.append(i)
print(newS_list)
