#A program to count the amount of even and odd numbers
evencount = 0
oddcount = 0
print("Please enter the first whole number.")
first = int(input())
print("Please enter the second whole number.")
second = int(input())
print("Please enter the third whole number.")
third = int(input())
if first % 2 == 0:
    evencount += 1
else:
    oddcount += 1

if second % 2 == 0:
    evencount += 1
else:
    oddcount += 1

if third % 2 == 0:
    evencount += 1
else:
    oddcount += 1

print("There were " + str(evencount) + " even and " + str(oddcount) + " odd numbers.")
