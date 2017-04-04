def pause():
    print('Press any key ...')
    inThing = None
    while inThing == None:
        inThing = input()

def collatz(number):
    if number % 2 == 0:
        out = number // 2
    else:
        out = 3 * number + 1
    print(out)
    return out

#get number and validate
numberStart = 0
errorMessage = "Must enter posivitive non-zero integer"

while numberStart < 1:
    try:
        print("Enter number: ", end='')
        numberStart = int(input())
        if numberStart < 1:
            print(errorMessage)
    except ValueError:
        print(errorMessage)
     
loopCount = 0

#run it
while numberStart > 1:
    loopCount = loopCount + 1
    numberStart = collatz(numberStart)

print("\nLoop Count:" + str(loopCount))   
#pause()
