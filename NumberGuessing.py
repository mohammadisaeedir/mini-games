# work together to find the number
import random
import math

lower = int(input('enter lower band: '))
upper = int(input('enter upper band: '))
print("you have only", round(math.log(upper-lower+1, 2)), "chances to win")
print('lets go to find the number')

realAnswer = random.randint(lower, upper)
# print(realAnswer)
playerPoint = round(math.log(upper-lower+1, 2))
while playerPoint > 0:
    playerGuess = int(
        input(f"left chances: {playerPoint} \nwhat is your guess? "))
    if playerGuess == realAnswer:
        print(
            f"thats right! the answer is {realAnswer} and your score: {playerPoint*20}")
        break
    elif playerGuess == realAnswer ** 2:
        print('division it')
        playerPoint -= 1
    elif playerGuess == realAnswer ** 0.5:
        print('multiple it')
    elif playerGuess < realAnswer:
        playerPoint -= 1
        print(f"greater")
        lower = playerGuess
        print(f"now between {lower} - {upper}")
        print
    elif playerGuess > realAnswer:
        playerPoint -= 1
        print(f"smaller")
        upper = playerGuess
        print(f"now between {lower} - {upper}")
if playerPoint == 0:
    print(f"You Lost, the answer was {realAnswer}")
