def isFusionShot(slug1, slug2):
    if slug1 == slug2:
        return True
    else:
        return False

def isDefectiveShot(slug1, slug2):
    if isFusionShot(slug1, slug2) == False:
        if (slug1 == "Infurnus" and slug2 == "Aquabeek") or (slug1 == "Aquabeek" and slug2 == "Infurnus"):
            print("true")
            return True
        else:
            print("false")
            return False
    else:
        print("false")
        return False

def run():
    print("Enter the first slug type:")
    slug1 = input()
    print("Enter the second slug type:")
    slug2 = input()
    print("Please make your choice - fusion or defective:")
    choice = input()
    if choice == "fusion":
        isFusionShot(slug1, slug2)
    elif choice == "defective":
        isDefectiveShot(slug1, slug2)
    else:
        print("Invalid selection. Please try again.")

# Run the programme
run()


