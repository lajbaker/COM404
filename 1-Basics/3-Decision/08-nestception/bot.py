#A program to help Beep find his battery
print("Where should I look?")
room = input()
if room == "in the bedroom":
    print("Where in the bedroom should I look?")
    bedroom = input()
    if bedroom == "under the bed":
        print("Found some shoes but no battery.")
    else:
        print("Found some mess but no battery.")
elif room == "in the bathroom":
    print("Where in the bathroom should I look?")
    bathroom = input()
    if bathroom == "in the bathtub":
        print("Found a rubber duck but no battery.")
    else:
        print("It is wet but I found no battery.")
elif room == "in the lab":
    print("Where in the lab should I look?")
    lab = input()
    if lab == "on the table":
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery")
else:
    print("I do not know where that is but I will keep looking.")