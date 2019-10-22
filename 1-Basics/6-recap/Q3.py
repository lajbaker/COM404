#while loop version
print("How many zones must I cross?")
zones = int(input())
print("Crossing zones...")

while zones > 0:
    print("...crossed zone", str(zones))
    zones -= 1

print("Crossed all zones. Jumanji!")

#for loop version
print("How many zones must I cross?")
zones = int(input())
print("Crossing zones...")

for zones in range(zones, 0, -1):
    print("...crossed zone", str(zones))

print("Crossed all zones. Jumanji!")