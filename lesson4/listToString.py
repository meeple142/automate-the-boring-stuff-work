def listToString(listIn):
    strOut = ''
    #loop all but the last one
    for item in listIn[0:-1]:
        strOut += str(item) + ', '
    #add on the word 'and' and then the last one
    strOut += 'and ' + str(listIn[-1])
    return strOut
    
def listToPrintStringDad(listIn):
    for i in range(len(listIn)-1):
        print(str(listIn[i]), end=', ')
    
    print("and " + str(listIn[-1]))
    
        
def listToPrintStringIf(listIn):
    for i in range(len(listIn)):
        if i != (len(listIn) -1):
            print(str(listIn[i]), end=', ')
        else:
            print("and " + str(listIn[i]))
    
#the lists I'm gunna use    
bestList = [1,3,3,3,3,3,3,2,3,4,5]
spam = ['apples', 'bananas', 'tofu', 'cats']

#print them 
print('My Way:')
print(listToString(bestList))
print(listToString(spam))
print('\nYour Way:')
listToPrintStringDad(bestList)
listToPrintStringDad(spam)
print('\nIf Way:')
listToPrintStringIf(bestList)
listToPrintStringIf(spam)