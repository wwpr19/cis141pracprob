
#2. Create a list of strings. Write code that counts how
#many times the word "Olympic" appears in the list, and then
#print the count.

O_list = ["olympic mountain","deer", "olympic beer","tomato", "olympic icerink", "fruit", "olympic college", "olympic dinner"]
count= 0 
newlist = []
for olympic in O_list:
    if "olympic" in olympic:
        
       newlist.append(olympic)
       count +=1
    else:
        print(olympic," :This isnt the word olympic")
       
print("New list:", newlist)
print("Count:", count)
