print("How many bars should be charged?")
print("")
total = int(input())
current = 0
print("")
while current < total:
    current = current + 1
    print("Charging: [" + str(current*"█") + str((total-current)*" ") + "]")
print("")
print("The battery is fully charged.")
