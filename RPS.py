import random

# Rock paper scissors
yourPoint = 0
myPoint = 0
list = ['r', 's', 'p']
print('are you ready? lets start')

while (myPoint or yourPoint) < 3:
     print(f"you: {yourPoint} | me: {myPoint}")
     player = input('Your Choice: ').lower()
     if player == ("q" or "quit"):
          print("as you wish, good luck")
          break
     myChoice = random.choice(list)
     print(f"My Choice: {myChoice}")
     if player == myChoice:
        print('equal')
     elif player == 'r':
        if myChoice == 'p':
            print('i won')
            myPoint += 1
        else:
            print('you win')
            yourPoint += 1
     elif player == 'p':
        if myChoice == 's':
            print('i won')
            myPoint += 1
        else:
            print('you win')
            yourPoint += 1
     elif player == 's':
        if myChoice == 'r':
            print('i won')
            myPoint += 1
        else:
            print('you win')
            yourPoint += 1
     else:
          print('try again....')

if (myPoint or yourPoint) == 3:
    print(f"you: {yourPoint} | me: {myPoint}")
    print('--------- * * * ---------')
    print('the game is finished')
