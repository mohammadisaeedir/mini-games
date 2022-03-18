import random
import termcolor2
import pyfiglet
# Basic Data
myNumbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
basicList = ["condition", "trip", "no", "good",
             "reviews", "wizard", "high", "service", "slow", "even", "friday",
             "restaurant", "full", "house", "salad", "come", "us",
             "event", "tasty", "board", "black"]
count = 0


print(termcolor2.colored('Are you ready? let begin',color='red'))
print(termcolor2.colored('if you need hint, enter "hint"', color='magenta'))
print(termcolor2.colored('if you want to exit, enter "exit"', color='magenta'))


def Convert(string):
    list1 = []
    list1[:0] = string
    return list1
# Driver code


finalAnswer = random.choice(basicList)
hintAnswer = Convert(finalAnswer)

chance = len(finalAnswer)
print('you have', chance, 'chance(s)')
# print(finalAnswer)


j = 0
hint = 1
notIn = []
for i in range(chance):
    notIn.append('-')
lst = []
for i in range(chance):
    lst.append('-')
print(lst)

while count < chance:
    guess = input('choose the letter? ').lower()
    while guess in myNumbers:
        guess = input('just letters must be entered, try again: ')
    while len(guess) != 1:
        guess = input('please enter at most one letter: ').lower()

    if all(lst[i] != '-' for i in range(chance)):
        print(f"excellent. you win, the answer is: {finalAnswer}")
        break

    
    for i in range(chance):
        if guess == (notIn[i] or lst[i]):
            print(f"try again, you have entered '{guess}' before")
# ---------------------
    if guess == 'exit':
        break
    if guess == 'hint':
        if hint > 0:
            filteredHint = filter(None, hintAnswer)
            print(f"Use: --  {random.choice(list(filteredHint))}  --")
            hint -= 1
        else:
            print('no more hint')
 # ------------------------
    
    for i in range(chance):
        if guess == finalAnswer[i]:
            lst[i] = guess
            hintAnswer[i] = None
    if all((guess != finalAnswer[i]) and (guess != notIn[i]) for i in range(chance)):
        notIn[j] = guess
        count += 1
        j += 1

    print(f" Word is: {lst}")
    print('----------------------------------------------')
    print(f" not in: {notIn} \n")
    # print(f" hint: {hintAnswer} \n")
    print(f"you have {chance - count} left chances \n")

    if 100*(chance-count)/chance <= 20:
        hint += 1
        print(pyfiglet.figlet_format(termcolor2.colored('congarulation, you have got 1 more hint, use it', color='blue')))

if count == chance:
    print(f"maybe next time, the answer is: '{finalAnswer}' \n")
