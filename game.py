import random

#get guess
def get_guess():
    return list(input("what is ur guess"))
#generate number
def generate_code():
    digits=[str(num) for num in range(10)]
    #shuffle the digits and grab first three
    random.shuffle(digits)
    return digits[:3]

#generate clues
def generate_clues(code, user_guess):
    if user_guess==code:
        return "code cracked"
    clues=[]
    for ind,num in enumerate(user_guess):
        if num==code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("close")
    if clues==[]:
        return ["nope"]
    else:
        return clues

#run game logic
print("Welcome Code Breaker!")
secret_code=generate_code()
clue_report=[]
while clue_report!="code cracked":
    guess=get_guess()
    clue_report=generate_clues(guess,secret_code)
    print("here is the result of your guess:")
    for clue in clue_report:
        print(clue)
