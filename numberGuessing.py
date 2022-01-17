import random
numbers = [1,2,3,4,5,6,7,8,9]
number = random.choice(numbers)
chances = 5
print("Number Guessing Game")
while (chances>0):
    question = input("Guess a number between 1 and 9 : ")
    answer = int(question)
    if(answer == number):
        print("You win")
        break 
    elif(answer>number):
        print("Guess something below ",answer)
        chances = chances-1
    elif(answer<number):
        print("Guess something above ",answer)   
        chances = chances-1
if(chances == 0):
    print("you lose!")
        
    
