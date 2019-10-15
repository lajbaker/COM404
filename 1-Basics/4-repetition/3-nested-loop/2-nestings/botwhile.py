print("Please enter a sequence:")
sequence = input()
print("Please identify the marker:")
marker = input()
negate = 0
distance = 0
for idx, letter in enumerate(sequence):
    if letter == marker:
        i = idx + 1
        while sequence[i] != marker:
            distance += 1
            i += 1
        break
print("The distance between the markers is", str(distance))       