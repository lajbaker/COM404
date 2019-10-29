print("How many heroes must we gather?")
heroes = int(input())
print("Gathering heroes...")
count = 1
for i in range(0,heroes,1):
    print("... found hero "+ str(count))
    count += 1
print("...all the heroes have been gathered")