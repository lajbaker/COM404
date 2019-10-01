#Program to identify whether we can find a match for a singleton.
print("Welcome to Beep's online dating tool. I will ask you a series of questions and hopefully find your perfect match!")
#Questionnaire
print("What is your age?")
age = int(input())
if age < 18:
    print("Your are too young to use this function.")
else:    
    print("Are you Male or Female?")
    gender = input()
    print("Are you interested in Men/Women/Both")
    interest = input()
    #catagories
    agebracket18to25malehet = 0
    agebracket26to35malehet = 0
    agebracket36plusmalehet = 0
    agebracket18to25femalehet = 0
    agebracket26to35femalehet = 0
    agebracket36plusfemalehet = 0
    agebracket18to25malehom = 0
    agebracket26to35malehom = 0
    agebracket36plusmalehom = 0
    agebracket18to25femalehom = 0
    agebracket26to35femalehom = 0
    agebracket36plusfemalehom = 0
    agebracket18to25malebi = 0
    agebracket26to35malebi = 0
    agebracket36plusmalebi = 0
    agebracket18to25femalebi = 0
    agebracket26to35femalebi = 0
    agebracket36plusfemalebi = 0
    #sorting the applicants into catagories
    if ((gender == "Male") and (interest == "Women")):
        if age >= 36:
            agebracket36plusmalehet =+ 1
        elif age >= 26:
            agebracket26to35malehet =+ 1
        else:
            agebracket18to25malehet =+ 1
    elif ((gender == "Male") and (interest == "Men")):
        if age >= 36:
            agebracket36plusmalehom =+ 1
        elif age >= 26:
            agebracket26to35malehom =+ 1
        else:
            agebracket18to25malehom =+ 1
    elif ((gender == "Male") and (interest == "Both")):
        if age >= 36:
            agebracket36plusmalebi =+ 1
        elif age >= 26:
            agebracket26to35malebi =+ 1
        else:
            agebracket18to25malebi =+ 1
    elif ((gender == "Female") and (interest == "Men")):
        if age >= 36:
            agebracket36plusfemalehet =+ 1
        elif age >= 26:
            agebracket26to35femalehet =+ 1
        else:
            agebracket18to25femalehet =+ 1
    elif ((gender == "Female") and (interest == "Women")):
        if age >= 36:
            agebracket36plusfemalehom =+ 1
        elif age >= 26:
            agebracket26to35femalehom =+ 1
        else:
            agebracket18to25femalehom =+ 1
    else:
        if age >= 36:
            agebracket36plusfemalebi =+ 1
        elif age >= 26:
            agebracket26to35femalebi =+ 1
        else:
            agebracket18to25femalebi =+ 1
#Deliver the bad news that they're the first to be added to the database (as I don't know how to loop the function yet)
    print("We have added your details to the system. We will be in touch when we have a suitable match bearing the following credentials:")
    if (((gender == "Male") and (interest == "Women")) or ((gender == "Female") and (interest == "Women"))):
        print("Gender - Female")
    elif (((gender == "Male") and (interest == "Men")) or ((gender == "Female") and (interest == "Men"))):
        print("Gender - Male")
    else:
        print("Gender - Both")

