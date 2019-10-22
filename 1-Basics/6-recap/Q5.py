health = 100
print("Your heath is " + str(health) + "%. Escape is in progress...")

for count in range(0,5,1):
    print("Oh dear, who is that?")
    response = input()
    if response == "Smilers Bot":
        print("Time to jam out of here!")
        health -= 20
    elif response == "Hacker":
        print("Yay! better follow this one!")
        health += 20
    else:
        print("Phew, just another emoji!")

print("Escaped. Health is ", str(health) + ".")