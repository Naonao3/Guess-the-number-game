import random

#start game
def startGame():
    print("Guess number!")
    print("Do you want to play game??")
    while True:
        choice = input("Input 'Yes' or 'No' --> ")
        choice = choice.lower()
        
        if choice == "yes":
            print("Let's start game!")
            inputNumber()
            break
        
        elif choice == "no":
            print("waiting your back...")
            break
        
        else:
            print("Please input 'Yes' or 'No' (；ﾟДﾟ)")
            continue

#input number you want
def inputNumber():
    mixNumber = int(input("Input the minimum number --> "))
    maxNumber = int(input("Input the maximum number --> "))
    
    while True:
        if mixNumber >= maxNumber:
            print("You inputed wrong number")
            print("maximum number is bigger than minimum number")
            inputNumber()
            break
        else:
            playGame(mixNumber,maxNumber)
            break

def playGame(minNumber,maxNumber):
    selectedAnswer = createRandomNumber(minNumber,maxNumber)
    howManyAnswer = numberOfAnswer()
    count = 1
    
    while count <= howManyAnswer:
        playerAnswer = int(input("plese input your guess number --> "))
        
        if not maxNumber >= playerAnswer >= minNumber:
            print("you should input number from " + str(minNumber) + " to " + str(maxNumber))
            
        elif playerAnswer == selectedAnswer:
            print("You are correct!!!")
            break
        else:
            print("you are wrong (◞‸◟)")
        
        remains = howManyAnswer - count
        if remains > 0:
            print("you can answer " + str(remains) + " more times")
        count += 1
    
#player has to guess this number
def createRandomNumber(minNUmber,maxNumber):
    result = random.randint(minNUmber,maxNumber)
    return result

#how many times player can answer from 1 to 10
def numberOfAnswer():
    result = random.randint(1,10)
    return result 

startGame()