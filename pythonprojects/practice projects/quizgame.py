questions = ("What is the biggest country?: ",
             "Who are you?: ",
             "Are you a motherfucker?: ",
             "What's the smallest country on earth?: ",
             "Fucker?: ")

options = (("A. Japan", "B. China", "C. Russia", "D. France"),
           ("A. Motherfucker", "B. RDJ", "C. THE ROCK", "D. McLean"),
           ("A. YES", "B. YES", "C. YES", "D. YES"),
           ("A. Batican", "B. Russia", "C. Vietnam", "D. DonkeyKong"),
           ("A. YES", "B. Of course", "C. I assume yes", "D. Hell ya!!"))

answers = ("C", "A", "B", "A", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+= 1
        print("CORRECT YOU MOTHERFUCKER")
    else:
        print("INCORRECT YOU MOTERFUCKER GET THE HELL OUT OF HERE YOU SON OF A BITCH")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("--------------")
print("   RESULTS    ")
print("--------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")

