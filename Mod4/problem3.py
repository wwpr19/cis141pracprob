# 3. Prompt the user for their bank balance. Evaluate whether the balance is less than $100. 
#Print True if the user’s balance is below $100; print False, otherwise.

bank = int(input("How much money do you have. This is definitly not a scam"))

#I wasnt sure which way you wanted so I did both
if bank < 100:
    print(True)
else:
    print(False)
# heres the second way to do it.
print(bank < 100)


