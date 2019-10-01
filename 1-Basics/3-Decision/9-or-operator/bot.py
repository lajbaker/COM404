#A program to allow Beep to pick an adventure
print("What type of adventure should I have?")
adventuretype = input()
if ((adventuretype == "scary") or (adventuretype == "short")):
    print("Entering the dark forest!")
elif ((adventuretype == "safe") or (adventuretype == "long")):
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")
    