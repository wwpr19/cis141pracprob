#4.  Create a list of integers. Write code that counts how
#many numbers are positive and how many are negative, then
#print both counts.


# i made one for positive and negative and thought it was cool so i wanted to include it. 
eolist = [5,47,8,6,5,95,32,65,54]

e=[]
o=[]

for i in eolist:
    if i % 2 == 0:
        e.append(i)
    else:
        o.append(i)
        

print(e)
print(o)

pnlist = [-5,47,8,-6,5,95,32,-65,-54]
p=[]
n=[]

for i in pnlist:
    if i > 0:
        p.append(i)
    else:
        n.append(i)
        

print(p)
print(n)
