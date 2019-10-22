word = input()
#delete variable before committing
def option_choice_1(word):
    print()
    print(word)
    print("*"*len(word))
    print()

def option_choice_2(word):
    print()
    print("*"*len(word))
    print(word)
    print()
    
def option_choice_3(word):
    print()
    print("*"*len(word))
    print(word)
    print("*"*len(word))
    print()

def option_choice_4(word):
    print("Please enter the amount of repetitions you wish to see:")
    n = int(input())
    print()
    for count in range(0,n,1):
        print("*"*len(word)+"   ", end="")
    print()
    for count in range(0,n,1):
        i = 1
        count2 = 0
        for count2 in range(0,n,1):
            if i < n:
                print(word, "| ", end="")
                i += 1
            else:
                print(word, end="")
        print()
        for count2 in range(0,n,1):
            print("*"*len(word)+"   ", end="")
        print()

option_choice_1(word)
option_choice_2(word)
option_choice_3(word)
option_choice_4(word)