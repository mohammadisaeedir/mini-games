import random
from termcolor2 import colored
from pyfiglet import figlet_format
# Basic Data
myNumbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
print(colored(figlet_format('Game Started'), color='yellow'))
print(colored('to use hint, type: hint', color='red'))
print(colored('to exit the game, type: exit', color='red'))

# guess = 'syamsak'
# guess = input('which word do you want to choose? ')

basicList = ["condition", "trip", "no", "good",
             "reviews", "wizard", "high", "service", "slow", "even", "friday",
             "restaurant", "full", "house", "salad", "come", "us",
             "event", "tasty", "board", "black"]
guess = random.choice(basicList)
hint = list(guess)  # hint list
hintCount = 1
answerList = []  # list of right answers
leftChance = []  # list of wrong answers
j = 0
for i in range(0, len(guess)):
    answerList.append('-')
    leftChance.append('-')
chance = 0

print(f'answerList: {answerList}')
print(f'leftChance: {leftChance}')

while chance <= len(guess):
    if len(list(filter(lambda x: x == '-', answerList))) == 0:
        print(colored(figlet_format('You win'), color='green'))
        break
    word = input(colored('pick your letter: ', color='blue')).lower()
    if word == 'hint':
        if hintCount > 0:
            print('the hint is', colored(random.choice(list(filter(lambda x: x != '-', hint))),color='red') )
            hintCount -= 1
        else:
            print('No more hint')

    elif word == 'exit':
        print('Thank you, Good luck')
        break
    elif len(word) > 1 or word in myNumbers:
        print('choos a letter please;')
    else:
        for i in range(len(guess)):
            if guess[i] == word:
                print(colored('correct!', color='green'))
                answerList[i] = word
                hint[i] = '-'
        if word not in leftChance and word not in guess:
            print(colored('oops, wrong!', color='red'))
            leftChance[j] = word
            j += 1
            chance += 1
        elif (word in answerList or word in leftChance) and word not in guess:
            print(colored('repeated one, choose another letter', color='yellow'))
        if chance == len(guess):
            print(colored(figlet_format('You Lose'), color='red'))
            print('the answer is:', colored(guess, color='cyan'))
            break

    print(f'answerList: {answerList}')
    print(f'leftChance: {leftChance}')
    # print(f'hint  list: {hint}')
