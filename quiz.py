user_score = 0  #sets the start score at zero
n = 7   #number of questions
correct = "Correct! +1 Points"  #write less code
incorrect = "Incorrect :("  #write less code 2
x = "What is the capital of "   #write less code 3

class qa:
    def __init__(self, nation, answer):
        self.nat = nation
        self.ans = answer

q1 = qa("france", "paris")
q2 = qa("thailand", "bangkok")
q3 = qa("germany", "berlin")
q4 = qa("austria", "vienna")
q5 = qa("japan", "tokyo")
q6 = qa("canada", "ottawa")
q7 = qa("mexico", "mexico city")

user_name = input("Hi, what is your name?   ")
yn = input(user_name.title() + " would you like to play a short trivia game?    ")

if yn.lower() == "yes":
    print("Awesome! " + user_name.title() + " let's get started!")
else:
    exit()

q_1 = input(x + q1.nat.title() + "? ")
if q_1.lower() == q1.ans.lower():
    print(correct)
    user_score = user_score + 1
else:
    print(incorrect)

q_2 = input(x + q2.nat.title() + "? ")
if q_2.lower() == q2.ans.lower():
    print(correct)
    user_score = user_score + 1
else:
    print(incorrect)

q_3 = input(x + q3.nat.title() + "? ")
if q_3.lower() == q3.ans.lower():
    print(correct)
    user_score = user_score + 1
else:
    print(incorrect)

q_4 = input(x + q4.nat.title() + "? ")
if q_4.lower() == q4.ans.lower():
    print(correct)
    user_score = user_score + 1
else:
    print(incorrect)

q_5 = input(x + q5.nat.title() + "? ")
if q_5.lower() == q5.ans.lower():
    print(correct)
    user_score = user_score + 1
else:
    print(incorrect)

q_6 = input(x + q6.nat.title() + "? ")
if q_6.lower() == q6.ans.lower():
    print(correct)
    user_score = user_score + 1
else:
    print(incorrect)

q_7 = input(x + q7.nat.title() + "? ")
if q_7.lower() == q7.ans.lower():
    print(correct)
    user_score = user_score + 1
else:
    print(incorrect)


print("Congrats! You have finished the quiz")
percent = (user_score / n) * 100
print("You achieved an accuracy of " + str(percent) + "%")
if user_score >= 6:
    print("You did better than most " + user_name.title() + "!")