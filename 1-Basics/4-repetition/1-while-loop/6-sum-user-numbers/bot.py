print("How many numbers should I sum up?")
repetitions = int(input())
current = 0
uservalue = 0
while current < repetitions:
    if uservalue < 1:
        current = current +1
        print("Please enter number " + str(current) + " of " + str(repetitions) + ":")
        uservalue = int(input())
    else:
        prevalue = uservalue
        current = current +1
        print("Please enter number " + str(current) + " of " + str(repetitions) + ":")
        uservalue = int(input())
        uservalue = uservalue + prevalue
print("The answer is " + str(uservalue))

    