
#4. Use nested for loops to create a simple multiplication 
#table for numbers 1 through 5. Format your output so that 
#each row corresponds to multiplying by a specific number. 
#Example output:

# 1   2   3   4   5
# 2   4   6   8   10
# 3   6   9   12  15
# 4   8   12  16  20
# 5   10  15  20  25

# This is my original way to run this code on my own. 
for a in range(1):
    for b in range(5):
        print((b+1) * 1, end=' ')
    print("")
    for c in range(5):
        print((c+1) * 2, end=' ')
    print("")
    for d in range(5):
        print((d+1) * 3, end=' ')
    print("")
    for e in range(5):
        print((e+1) * 4, end=' ')
    print("")
    for f in range(5):
        print((f+1) * 5, end=' ')
    print("")
    print("The end of the loop")
    
print("AI code")
# i included this because its a cleaner version then what i originaly did. It is AI generated. 
for row in range(1, 6):
    for col in range(1, 6):
        print(row * col, end=' ')
    print("")
