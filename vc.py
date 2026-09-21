# AI Vacuum Cleaner


rooms = {
    "A": "Dirt",
    "B": "Dirt"
}


rooms["A"] = input("Enter condition of Room A (Clean/Dirt): ")
rooms["B"] = input("Enter condition of Room B (Clean/Dirt): ")


position = input("Enter vacuum cleaner position (A/B): ").upper()

print("\nVacuum Cleaner Started")
print("----------------------")


while rooms["A"].lower() == "dirt" or rooms["B"].lower() == "dirt":

    print("\nVacuum is in Room", position)

    if rooms[position].lower() == "dirt":
        print("Room", position, "is Dirty")
        print("Action: Suck")
        rooms[position] = "Clean"

    else:
        print("Room", position, "is Clean")

        if position == "A":
            print("Action: Move Right to Room B")
            position = "B"
        else:
            print("Action: Move Left to Room A")
            position = "A"

print("\nBoth rooms are Clean.")
print("Vacuum Cleaner Stopped.")