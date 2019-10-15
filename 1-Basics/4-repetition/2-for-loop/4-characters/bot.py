print("What strange markings do you see?")
markings = input()
print("Indentifying...")
for position in range(0, len(markings), 1):
    print("Index " +str(position) + ": " + markings[position])
print("Done!")
for idx, marking in enumerate(markings):
    print("Index " +str(idx) + ": " + marking)