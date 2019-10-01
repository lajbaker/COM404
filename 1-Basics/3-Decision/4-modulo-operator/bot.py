#A program to define whether a number is even or odd.
print("Please enter a whole number.")
wholenumber = int(input())
if int(wholenumber) % 2 != 0:
    print("The number " + str(wholenumber) + " is an odd number.")
else:
    print("The number " + str(wholenumber) + " is an even number.")
