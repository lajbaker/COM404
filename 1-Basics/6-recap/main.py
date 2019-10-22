
from functions import option_choice_1, option_choice_2, option_choice_3, option_choice_4

print("Please enter a word:")
word = input()
print("Please read through the following options:")
print("Option 1: Under - display your word with a line under it.")
print("Option 2: Over - display the word with a line over it.")
print("Option 3: Both - display the word in an underline and overline.")
print("Option 4: Grid - display the word in a grid that is n x n in size.")
print()
print("Please make your choice by entering the option number (1 to 4)")
while True:
    try:
        option = int((input))
    except ValueError:
        print("Please enter a number between 1 and 4:")
if option == 1:
    option_choice_1(word)
elif option == 2:
    option_choice_2(word)
elif option == 3:
    option_choice_3(word)
elif option == 4:
    option_choice_4(word)
else:
    print("Invalid option.")