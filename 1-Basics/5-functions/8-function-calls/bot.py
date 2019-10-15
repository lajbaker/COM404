#Display in a Box - display the word in an ascii art box
def box_display(word):
    print("*" * (len(word) + 4))
    print("*", word, "*")
    print("*" * (len(word) + 4))

#Display Lower-case – display the word in lower-case e.g. hello
def lower_case_display(word):
    print(word.lower())

#Display Upper-case – display the word in upper-case e.g. HELLO 
def upper_case_display(word):
    print(word.upper())

#Display Mirrored – display the word with its mirrored word e.g. Hello | olleH
def mirrored_display(word):
    print(word + " | ", end="")
    for position in range(len(word)-1,-1,-1):
        print(word[position], end="")
    print("")

#Repeat – ask the user how many times to display the word and then display the word that many times alternating between upper-case and lower-case.
def repeat_display(word):
    print("How many times should I display the word?")
    loopamt = int(input())
    index = 0
    for count in range(loopamt):
        if index % 2 == 0:
            print(word.lower())
        else:
            print(word.upper())
        index += 1
        
def run():
    print("Please choose one of the following options:")
    print("1) Display in a Box – display the word in an ascii art box")
    print("2) Display Lower-case – display the word in lower-case e.g. hello")
    print("3) Display Upper-case – display the word in upper-case e.g. HELLO")
    print("4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH")
    print("5) Repeat – ask the user how many times to display the word and then display the word that many times alternating between upper-case and lower-case.")
    print("Please enter an option (1 to 5):")
    choice = input()
    print()
    print("What is the word?")
    word = input()
    print()
    if choice == "1":
        box_display(word)
    elif choice == "2":
        lower_case_display(word)
    elif choice == "3":
        upper_case_display(word)
    elif choice == "4":
        mirrored_display(word)
    elif choice == "5":
        repeat_display(word)
    else:
        print("Invalid Choice")
#Run the Program
run()