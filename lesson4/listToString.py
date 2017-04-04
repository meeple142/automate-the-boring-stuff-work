def listToString(listIn):
    strOut = ''
    #loop all but the last one
    for item in listIn[0:-1]:
        strOut += str(item) + ', '
    #add on the word 'and' and then the last one
    strOut += 'and ' + str(listIn[-1])
    return strOut
    
bestList = [1,3,3,3,3,3,3,2,3,4,5]

spam = ['apples', 'bananas', 'tofu', 'cats']

print(listToString(bestList))
print(listToString(spam))