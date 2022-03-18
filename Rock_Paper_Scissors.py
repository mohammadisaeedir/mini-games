
import random
print("Time to have fun")

playerPoint = 0
myPoint = 0

print(f"result : {myPoint} - {playerPoint} ")

while (playerPoint and myPoint) < 3 :
    
     player = input("Your Turn: \n").lower()
     if player == ('q' or 'quit'):
          print('the game is finished...')
          break
     print("My Turn")
     myTurn = random.choice(['rock','paper','scissors'])
     print(myTurn)
     if player == myTurn :
          print("equal, play again")
          print(f"result : {myPoint} - {playerPoint} ")
     elif player == "rock" :
          if myTurn == "scissors" :
               print("You are locky, next time")
               playerPoint += 1
               print(f"result : {myPoint} - {playerPoint} ")
          elif myTurn == "paper":
               print("i told you, easy peasy to beat you")
               myPoint +=1
               print(f"result : {myPoint} - {playerPoint} ")
     elif player == "scissors" :
          if myTurn == "paper" :        
               print("You are locky, next time")
               playerPoint += 1
               print(f"result : {myPoint} - {playerPoint} ")
          elif myTurn == "rock":
               print("i told you, easy peasy to beat you")
               myPoint +=1
               print(f"result : {myPoint} - {playerPoint} ")
     elif player == "paper" :
          if myTurn == "rock" :
               print("You are locky, next time")
               playerPoint += 1
               print(f"result : {myPoint} - {playerPoint} ")
          elif myTurn == "scissors":
               print("i told you, easy peasy to beat you")
               myPoint +=1
               print(f"result : {myPoint} - {playerPoint} ")
     else :
          print("Something went wrong, play again")
          print(f"result : {myPoint} - {playerPoint} ")

if   playerPoint == 3:
     print("************* Finish *************")
     print("i Lost, You are Hero")
elif myPoint == 3:
     print("************* Finish *************")
     print("I Won, Go Fuck Yourself")
          



