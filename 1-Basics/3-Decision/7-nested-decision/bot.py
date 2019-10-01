#A program to help Beep classify his books.
print("What type of cover does the book have?")
cover = input()
if cover == "soft":
    print("Is the book perfect bound?")
    bind = input()
    if bind == "yes":
        print("Soft cover, perfect bound books are very poular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
elif cover == "hard":
    print("Books with hard covers can be more expensive!")
else:
    print("I'm having a hard time classifying this book!")
