class Bot:
    def __init__(self, name, age, energy, weight):
        self.name = name
        self.age = age
        self.energy = energy
        self.shield = weight
    
    def display_name(self):
        print("-" + "-"*len(self.name) + "-")
        print("|{}|".format(self.name))
        print("-" + "-"*len(self.name) + "-")

    def display_age(self):
        print("    iiiiiiiiii")
        print("   |:H:a:p:p:y:|")
        print(" __|___________|__")
        print("|^^^^^^^^^^^^^^^^^|")
        print("|:B:i:r:t:h:d:a:y:|")
        print("|       {}!       |".format(self.age))
        print("~~~~~~~~~~~~~~~~~~~")

    def display_energy(self):
        print("Energy: "+ (self.energy*"♦"))

    def display_shield(self):
        print(" ________ ")
        print("/        \\")
        print("| Shield |")
        print("\\   is   /")
        print(" \\  {}  /".format(self.shield))
        print("  \\    /")
        print("   \\  /")
        print("    \\/")

    def display_summary(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Energy: " + (self.energy*"♦"))
        print("Shield: " + (self.shield*"♦"))
    
    def __str__(self):
        return("{} is {} years old, has {} energy and {} shield.".format(self.name, self.age, self.energy, self.shield))
    
bot = Bot("Bot", 27, 5, 15)

bot.display_name()

bot.display_age()

bot.display_energy() 

bot.display_shield()

bot.display_summary()

print(bot.__str__())

