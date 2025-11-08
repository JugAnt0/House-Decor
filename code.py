import random
import time

print("Welcome to Antonio's House Decor Service (digital edition)!")
time.sleep(2)

rooms = {
    1: ("Living Room", 
        ["sofa", "coffee table", "TV stand", "bookshelf", "armchair"],
        ["modern", "rustic", "minimalist", "bohemian, industrial"]),
    2: ("Bedroom", 
        ["bed", "wardrobe", "nightstand", "dresser", "desk"],
        ["contemporary", "vintage", "scandinavian", "eclectic", "traditional"]),
    3: ("Kitchen", 
        ["kitchen island", "bar stools", "pantry", "dining table", "cabinetry"],
        ["farmhouse", "coastal", "transitional", "art deco", "mid-century modern"]),
    4: ("Bathroom", 
        ["vanity", "shower", "bathtub", "toilet", "storage cabinet"],
        ["spa-like", "classic", "modern", "eclectic", "rustic"]),
    5: ("Backyard", 
        ["patio set", "grill", "garden bench", "fire pit", "hammock", "gazebo"],
        ["tropical", "zen", "cottage", "mediterranean", "modern"])
}

while True:
    print("\n----- ROOM SELECTION -----")
    time.sleep(1)
    for num, data in rooms.items():
        print(f"{num}. {data[0]}")
    print("6. Choose for me")

    choice = int(input("Which room would you like to decorate? (1-6): "))

    if choice == 6:
        choice = random.randint(1, 5)

    if choice in rooms:
        room_name, furniture, styles = rooms[choice]
        print(f"\nGreat! You chose the {room_name}.")
        time.sleep(1)

        style = input(f"Choose an interior style {styles}: ")
        time.sleep(1)

        main_piece = random.choice(furniture)
        secondary_1 = random.choice(furniture)
        secondary_2 = random.choice(furniture)

        print(f"\nYour {style} {room_name.lower()} will feature a {main_piece} as the centerpiece.")
        time.sleep(2)
        print(f"It will be complemented by a {secondary_1} and a {secondary_2} to complete the look.")
        time.sleep(3)
        print("\nReturning to Room Selection...")
        time.sleep(2)

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
        time.sleep(2)
