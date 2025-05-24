
#5. Write a function called level_up(experience) that takes 
#a player's experience
#points and returns their new level based on these rules:
#* 0-99 XP → Level 1
#* 100-199 XP → Level 2
#* 200+ XP → Level 3

def level_up(experience):

    if experience <= 99:
        return 1
    elif experience >= 200:
        return 3 
    else:
        return 2




print("player 1 your level is at",level_up(56))
print("player 2 your level is at",level_up(143))
print("player 3 your level is at",level_up(345))
