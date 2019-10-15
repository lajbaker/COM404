def sum_weights(BeepW, BopW):
    total = BeepW + BopW
    return total

def calc_avg_weight(BeepW, BopW):
    avg = (BeepW + BopW)/2
    return avg

def run():
    print("What is the weight of Beep?")
    BeepW = int(input())
    print("What is the weight of Bop?")
    BopW = int(input())
    print("What would you like to calculate (sum or average)?")
    decision = input()
    if decision == "sum":
        print("The sum of Beep and Bop's weight is " + str(sum_weights(BeepW, BopW)))
    elif decision == "average":
        print("The average of Beep and Bop's weight is " + str(calc_avg_weight(BeepW, BopW)))
    else:
        print("invalid answer.")

run()
