import random
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
c=random.randint(a,b)
e=1
print("Player 1:")
while True:
    d=int(input("Guess the number: "))
    if d==c:
        print("This is the correct guess")
        print("You Won")
        print(f"You take {e} chance to win")
        break
    elif d<c:
        print("The number is greater than the guess number")
        e=e+1
    elif d>c:
        print("The number is smaller than the guess number")
        e=e+1
g=random.randint(a,b)
f=1
print("Player 2:")
while True:
    d=int(input("Guess the number: "))
    if d==g:
        print("This is the correct guess")
        print("You Won")
        print(f"You take {f} chance to win")
        break
    elif d<g:
        print("The number is greater than the guess number")
        f=f+1
    elif d>g:
        print("The number is smaller than the guess number")
        f=f+1   
if f==e:
    print("The game is tie")
elif f>e:
    print("Player 1 won the game")
else:
    print("Player 2 won the game")