def visit(ghost):
    if ghost == "ghost of christmas past":
        print("Humbug! I care not for these days of past celebration.")
    elif ghost == "ghost of christmas present":
        print("Humbug! I care not for their suffering.")
    elif ghost == "ghost of christmas future":
        print("Please no more. I will change my ways.")
    else:
        print("invalid ghost...")
visit("ghost of christmas past")
visit("ghost of christmas present")
visit("ghost of christmas future")