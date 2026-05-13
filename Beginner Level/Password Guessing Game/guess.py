import random 

easy_words = [
    "cat",
    "dog",
    "sun",
    "moon",
    "book",
    "pen",
    "tree",
    "fish",
    "ball",
    "home"
]
medium_words = [
    "school",
    "family",
    "friend",
    "garden",
    "window",
    "laptop",
    "mobile",
    "market",
    "office",
    "coffee"
]
hard_words = [
    "siyamahmed",
    "computer",
    "elephant",
    "building",
    "Dipanwita"
    "language",
    "password",
    "mountain",
    "electric",
    "umbrella",
    "chocolate",
    "notebook"
]

print("Welcome to the password guessing game")
print("Choose a difficulty level :easy,medium or hard")

level=input("Enter Difficulty level: ").lower()

if level == "easy":
    secret=random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level=="hard":
    secret=random.choice(hard_words)

else:
    print("Invalid choice,defaulting to easy words")
    secret=random.choice(easy_words)

attempts=0
print("\nGuess the secret password!")

while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1

    if guess == secret:
        print(f"Congrats!You guessed it right in {attempts} attempts")
        break
    else:
        hint = ""
        for i in range(len(secret)):
            if i < len(guess) and guess[i] == secret[i]:
                hint += guess[i]
            else:
                hint += "_"
        print("Hint:", hint)

print("Game Over!")
        
        
