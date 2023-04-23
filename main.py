# Quiz

# You can edit the questions here
questions = ("What is October's birthstone?: ",
             "How long is my (4/23/23) duolingo streak?: ",
             "When was Hiroshima bombed by the US? (What number day ex. 17): ",
             "How old is Mojo(my cat)?: ",
             "How many planets are in the solar system?: ",)

# You can edit the options here
options = (("A. Diamond", "B. Opal", "C. Quartz", "D. Aquamarine"),
           ("A. 22", "B. 6", "C. 15", "D. 21"),
           ("A. 6", "B. 14", "C. 9", "D. 7"),
           ("A. 7", "B. 8", "C. 9", "D. 10"),
           ("A. 8", "B. 11", "C. 9", "D. 7"))

# You can choose the answers here
answers = ("B", "D", "A", "C", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------")
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
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("-----------------------")
print("        RESULTS        ")
print("-----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end="")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
