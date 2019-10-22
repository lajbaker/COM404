def is_league_united(hero1, hero2):
    
    if (hero1 == "Superman" and hero2== "Wonder Woman") or (hero2 == "Superman" and hero1 == "Wonder Woman"):
        return True
    else:
        print("meh")
        return False
def decide_plan(hero1, hero2):
    if is_league_united(hero1, hero2) == True:
        print("Time to save the world!")
    else:
        print("We must unite the league!")
def run():
    print("enter the name of the first hero:")
    hero1 = input()
    print()
    print("enter the name of the second hero:")
    hero2 = input()
    print()
    print("Would you like to know if the league is united (enter: league) or shall we decide on a plan (enter: plan)")
    choice = input()
    if choice == "league":
        is_league_united(hero1, hero2)
    elif choice == "plan":
        decide_plan(hero1, hero2)
    else:
        print("Invalid Command. Please try again.")

run()
    
