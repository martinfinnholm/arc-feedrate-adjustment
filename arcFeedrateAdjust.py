def user_input(prompt):
    while True:
        try:
            user_flt = float(input(prompt))
        except ValueError:
            print("Value error, please enter a valid number.")
        else:
            break
    return user_flt


print("Internal arc adjustment calculator\n")
adjusted_feed = None
while adjusted_feed is None:

    linear_feed = user_input("Linear feed: ")
    major_dia = user_input("Major diameter: ")
    cutter_dia = user_input("Cutter diameter: ")

    adjusted_feed = linear_feed * ((major_dia - cutter_dia) / major_dia)
    print(("F" + str(round(adjusted_feed, 2))))


