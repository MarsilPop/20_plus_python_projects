questions = ("How many rings were given to the Elves in LOTR?",
             "How many rings were given to the Dwarfs in LOTR?",
             "How many rings where given to the Humans in LOTR?",
             "Who is the father of Legolas?",
             "What do the Elves call Gandalf the Grey?")

options = (("A. 4", "B. 3", "C. 9", "D. 7"), 
           ("A. 4", "B. 3", "C. 9", "D. 7"), 
           ("A. 4", "B. 3", "C. 9", "D. 7"), 
           ("A. Lord Elrond", "B. King Thranduil", "C. Sauron", "D. Gimli"), 
           ("A. White Rider", "B. Old Greybeard", "C. Mithrandir", "D. Incánus"))

answers = ("B", "D", "C", "B", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1

print("--------------------")
print("      RESULTS       ")
print("--------------------")

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
