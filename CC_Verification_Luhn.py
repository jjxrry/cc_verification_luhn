#This program takes in a string input between 13-16 digits to verify
#if the credit card number is valid

#Input/Processing/Output
#Asks user for 13-16 character range input

def main():

    userInput = int(input("How many credit card numbers do you want to check? "))
        
    for i in range(userInput):
            
            cardNum = str(input("Enter a credit card number: "))
            
            if isValid(cardNum) == True:
                print(cardNum, "is valid")
                
            else:
                print(cardNum, "is invalid")


    while userInput == 0:
        userInput = int(input(""))

def isValid(cardNum: str) -> bool: #receives cardNum
    ''' checks if the input is a valid credit card number '''
    cardLen = False
    cardFirst = False
    numValid = False

    if len(cardNum) >= 13 and len(cardNum) <= 16:
        cardLen = True
        
    if cardNum[0] == "4" or cardNum[0] == "5" or cardNum[0] == "6" or (cardNum[0] == "3" and cardNum[1] == "7"):
        cardFirst = True

    sumEven = sumOfDoubleEvenPlace(cardNum)
    sumOdd = sumOfOddPlace(cardNum)
    
    if ((sumEven) + (sumOdd)) % 10 == 0: #checks in a and b+c is true
        numValid = True

    if cardLen and cardFirst and numValid == True:
        return True
    else:
        return False    #how to return this bool value to main()

    

def sumOfDoubleEvenPlace(cardNum: str):
    ''' takes every even place number of cardNum *2 and checks if the sum of those 2 integers <= 9 '''
    result = 0
    for i in range(len(cardNum) -2,-1,-2):
        result += getDigit((int(cardNum[i]) * 2))  #calls getDigit
    return result


def getDigit(result: int) -> int:
    ''' receives result to check <= 9 '''
    if result >= 10:
        result = ((result % 10) + (result // 10 % 10))
    return result   #Return digit

    if result <= 9:
        return result



def sumOfOddPlace(cardNum: str):
    ''' takes the value of every odd place number of cardNum and returns the sum of all int '''
    result = 0
    for i in range(len(cardNum) -1,-1,-2):
        result += int(cardNum[i])
    return result


if __name__ == "__main__":
    main()
