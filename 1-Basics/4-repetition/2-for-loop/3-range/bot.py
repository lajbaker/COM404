print("What level of brightness is required?")
brightness = int(input())
print("Adjusting brightness...")
for count in range(2,(brightness+2),2):
    print("Beep's brightness level: " + str(count *"*"))
    print("Bop's brightness level: " + str(count *"*"))
print("Adjustments Complete!")