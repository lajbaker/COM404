def spideySense(enemy, direction):
    if enemy == "Green Goblin":
        print("Goblin bombs incoming from " + direction + ".")
    elif enemy == "Venom":
        print("Venemous webbing incoming from " + direction + ".")
    elif enemy == "Electro":
        print("Electro striking from " + direction + ".")
    else:
        print("New enemy attacking from " + direction + ".")

# The following are calls to the function for testing purposes
spideySense("Green Goblin", "front")
spideySense ("Venom", "behind")
spideySense ("Electro", "left side")
spideySense ("Unknown", "right side")