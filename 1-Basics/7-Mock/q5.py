print("Welcome to the Planet of the Apes...")
human = 0
ape = 0
for i in range(0,7,1):
    print("...be ye human or be ye ape?")
    answer = input()
    if answer == "Human":
        print("I did not start this war. But I will finish it.")
        human += 1
    elif answer == "Ape":
        print("Apes together strong!")
        ape += 1
    else:
        print("This is not your fight.")

print("Total humans encountered: " + str(human))
print("Total apes encountered: " + str(ape))
