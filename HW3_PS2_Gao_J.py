#Jerry Gao
#ID 1028410
#HW 3
#Program Set 2
#This program takes in a string input between 13-16 digits to verify
#if the credit card number is valid

#Input
#Asks user for 13-16 character range input
#Processing/Output
#Def functions to process sumOfDoubleEvenPlace and sumOddPlace sends results to isValid to
#
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


##Test Run 1
##
##How many credit card numbers do you want to check? 2
##Enter a credit card number: 4388576018402626
##4388576018402626 is invalid
##Enter a credit card number: 4388576018410707
##4388576018410707 is valid
##
##
##Test Run 2
##
##How many credit card numbers do you want to check? 0
##
##
##Test Run 3
##
##How many credit card numbers do you want to check? 3
##Enter a credit card number: 12345678
##12345678 is invalid
##Enter a credit card number: 5169769005222217
##5169769005222217 is valid
##Enter a credit card number: 6011655276746808
##6011655276746808 is invalid
##
##
##Test Run 4
##
##How many credit card numbers do you want to check? 2
##Enter a credit card number: 7288827161122235
##7288827161122235 is invalid
##Enter a credit card number: 374007272716930
##374007272716930 is valid
##
##
##Test Run 5
##
##How many credit card numbers do you want to check? 4
##Enter a credit card number: 374700272713960
##374700272713960 is valid
##Enter a credit card number: 6011405517534751
##6011405517534751 is valid
##Enter a credit card number: 6011504557135741
##6011504557135741 is valid
##Enter a credit card number: 342462964238231
##342462964238231 is invalid


