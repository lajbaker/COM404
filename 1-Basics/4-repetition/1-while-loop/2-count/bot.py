print("How many cables must I avoid?")
livecable = 0
avoid = int(input())
while (livecable < avoid):
    livecable = livecable + 1
    print("avoiding...Done! ", livecable, "live cables avoided.")
print("All live cables have been avoided.")
