InitHeight = 100
BounceRatio = .6

numBounces = 0
ballHeight = InitHeight

while numBounces < 10:
    ballHeight = ballHeight * BounceRatio
    numBounces = numBounces + 1
    print ("Bounce", numBounces, ": ", round(ballHeight,4))

