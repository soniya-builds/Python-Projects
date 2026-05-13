import random
subjects= [" Sheikh Hasina",
"Obaidul Qader",
"Ananta Jalil",
"Your ex",
"Hero Alom",
"Auto Wala mama",
"A group of monkeys",
"Blue Fairy Laila",
"Sakib Al Hasan",
"Virat Kohli",
"Shah Rukh Khan"]

Actions=[
    "launces",
    "cries",
    "dances",
    "jumps",
    "shakes",
    "declares war on",
    "celebrates",
    "cancels"
]

places_of_things=[
    "at Dhaka University",
    "at Shahbag",
    "at Ganavaban",
    "at Iblish Chattar",
    "at Amchattar",
    "in local train",
    "in a plate of velpuri",
    "in BPL",
    "at Mawa ghat"
]

while True:
    subject=random.choice(subjects)
    Action=random.choice(Actions)
    places_of_thing=random.choice(places_of_things)

    headline = f"BREAKING NEWS: {subject} {Action} {places_of_thing}"
    print("\n"+headline)
    
    user_input=input("\nDo you want another headline?(yes/no)").strip().lower()

    if user_input == "no":
        break

print("\n Thanks for yousing fake headline generator")