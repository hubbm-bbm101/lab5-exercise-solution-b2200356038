import random
number=random.randint(1,100)
while True:
    guess=int(input("Make a guess"))
    if(guess>number):
        print("decreasing")
    elif (guess<number):
        print("increasing")
    else:
        print("Correct!")