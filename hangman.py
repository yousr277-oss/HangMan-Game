import random
Words= ["python", "code", "alpha", "physics", "content", "egypt"]
secret_word =random.choice(Words)
word_display = ["_"] * len(secret_word) 
attempts = 6
guessed_letters = []
print("=== Welcome in HangMan game===")
while attempts > 0 and "_" in word_display:
    print ("\n -----------------------------")
    print ("current word is: " + " ".join(word_display))
    print(f"remaining attempts is: {attempts}")
    guess= input("Enter a letter:").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Entschuldigung, bitte versuchen Sie er noch einmal")
        continue 
    guessed_letters.append(guess)

    if guess in secret_word:
        print (f"exzellent, the leeter '{guess}' is in the word")
        for i in range(len(secret_word)):
          if secret_word[i] == guess :
            word_display[i] = guess
    else :
        print (f" the letter {guess} is not found")
        attempts = attempts - 1
print("\n=====================")
if "_" not in word_display:
    print(f"congratulations, the word is {secret_word}")
else:
    print (f"Game over!, the right word is{secret_word}")