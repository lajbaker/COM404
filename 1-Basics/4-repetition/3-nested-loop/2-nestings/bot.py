print("Please enter a sequence:")
sequence = input()
print("Please identify the marker:")
marker = input()
negate = 0
distance = 0
for position in range(0,len(sequence),1):
    if sequence[position] != marker:
        negate = negate +1
    else:
        for i in range(negate + 1, len(sequence), 1):
            if sequence[i] != marker:
                distance = distance + 1
            else:
                break
        break
print("The distance between the markers is ", str(distance))               