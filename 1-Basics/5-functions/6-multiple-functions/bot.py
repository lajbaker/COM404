def display_ladder(steps):
    for count in range(steps):
        print("| |")
        print("***")
    print("| |")
def create_ladder():
    print("How many steps remain?")
    steps = int(input())
    print()
    display_ladder(steps)

create_ladder()
