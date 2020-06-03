

print("This program will calculate the scrabble value for any given word\n")
again = 'Y'

while again == 'Y':
    word = input("Enter a word:    ").lower()
    score = 0

    for w in word:
        if w in 'aeioulnstr':
            score += 1
        elif w in 'dg':
            score += 2
        elif w in 'bcmp':
            score += 3
        elif w in 'fhvwy':
            score += 4
        elif w == 'k':
            score += 5
        elif w in 'jx':
            score += 8
        elif w in 'qz':
            score += 10

    print(f"The score for this word is: {score}")
    again = input("Go again? (Y/N)     ").strip().upper()