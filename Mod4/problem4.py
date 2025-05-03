# 4. A theater wants to enforce age restrictions for movie tickets. Ask the user for their age,
#and tell them whether they
#can see G (appropriate for under 13), PG-13 (appropriate for 13 to 17),
# or R (appropriate for over 18) rated movies.


age = int(input("How old are you?"))
if age <13:
    print("they can see rated G movies")
elif  13 <= age <=17:
    print("they can see rated PG-13 movies")
else:
    print("they can see rated R movies")
