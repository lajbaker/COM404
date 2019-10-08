print("Please enter a number:")
userno = int(input())
factorial = userno
repetition = 1
while repetition < userno:
    multiplier = userno - 1
    factorial = factorial * multiplier
    userno = multiplier
print("The factorial is " + str(factorial) + ".")