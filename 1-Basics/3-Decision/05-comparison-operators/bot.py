#A program to identify which number is the smallest.
print("Please enter the first number.")
first = int(input())
print("Please enter the second number.")
second = int(input())
if first > second:
    print("The second number is the smallest!")
elif first < second:
    print("The first number is the smallest!")
else:
    print("Both are equal!")
