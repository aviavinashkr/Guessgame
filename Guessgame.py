lucky=24
guess=1
score =20
glist=[]
while score>=3:
    guess=int(input("Enter the Guess"))


    if guess==lucky:
        print("You have won!!")

        break
    elif guess>lucky:
        print("Choose something lesser!!")
        score=score-3

    else:
        print("Choose somethng larger!!")
        score=score-3

    print("Points left ",score)
    glist.append(guess)
    print("Your guess numbers",glist)

