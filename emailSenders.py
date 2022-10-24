import sys

# controls the display of helper messages 
_DEBUG = False
_MENU_SIZE = 8  


def process_mail_file(fName, mDict):
    # open the file 
    fHandle = open(fName)

    # in a loop check for lines that start with "From "
    for fLine in fHandle:
        if( fLine[0:5] == "From " ):
            # the line template is From prefix@domain.xx Day Mon date time
            # extract the prefix@domain part, i.e. from the 6th character until the first space after that 
                # split the line into words, and select the second word
            if(_DEBUG): print("Processing line: ", fLine)
            fLineWords = fLine.split()
            emailAddress = fLineWords[1]
    
            # call a function to add information to a dictionary
            process_email_address(emailAddress, mDict)

    # close the file after all the lines are processed
    fHandle.close()



# function to add data to the dictionary
def process_email_address (emailAddr, mDict):
    if(_DEBUG): print("Process email address: ", emailAddr)
    eParts = emailAddr.split('@')
    prefix = eParts[0]
    domain = eParts[1]
    # if prefix exists, increment the count. If not, create new entry
    if( prefix in mDict):
        if(_DEBUG): print("Incrementing existing key: ",prefix)
        mDict[prefix] = mDict[prefix] + 1
    else:
        if(_DEBUG): print("Adding new key: ", prefix)
        mDict[prefix] = 1



# function to create a message with dictionary stats
def dictStats(mDict):
    countSenders = len(mDict)
    countEmails = 0
    topSender = None
    topEmails = None
    for (dictKey,dictVal) in mDict.items():
        countEmails = countEmails + dictVal
        if( topEmails is None or topEmails < dictVal):
            topEmails = dictVal
            topSender = dictKey

    avgEmails = 0
    if (countSenders > 0): avgEmails = countEmails / countSenders

    msg = "The file contains: \n\t {0} emails \n\t {1} senders \n\t {2:.2f} emails per sender on average. \nMost emails were sent by {3}  ({4})."
    msg = msg.format(countEmails, countSenders, avgEmails, topSender, topEmails )

    return msg


# function to list senders in natural state
def printDict(mDict):
    if(_DEBUG): print(mDict)

    print(mDict.items())

    print() #separation line
    print("Senders and emails count:") 
    for (mKey, mValue) in mDict.items():
        print(mKey, ": ", mValue)



# function to list senders alphabetically
def printDictAlphaSorted(mDict, reversed = False):
    print("Senders sorted alphabetically")
    print(sorted(mDict.keys(), reverse=reversed))


# function to list senders by number of emails sent
def printDictSendSorted(mDict, reversed = False):
    print("Number of emails sent, sorted")
    print(sorted(mDict.values(), reverse=reversed))



# function to display the key/values sorted by number of emails
def printDictSortedPairs(mDict):
    tmpList = list()
    for (dictKey,dictVal) in mDict.items():
        tmpList.append((dictVal, dictKey))
    
    # sort and print
    tmpList = sorted(tmpList, reverse=True)
    for (key, val) in tmpList:
        print(val, ": ", key)
    


# function to display the menu and ask the user for input
def displayMenu():
    print("\n\nChoose an action")
    print("\t 1. Dictionary statistics")
    print("\t 2. List items")
    print("\t 3. List senders alpha-sorted")
    print("\t 4. List senders reversed alpha-sorted")
    print("\t 5. List number of emails sent, sorted")
    print("\t 6. List number of emails sent, reversed sorted")
    print("\t 7. List key/value pairs sorted")
    print("\t 8. EXIT")
    print()
      
    mySelInt = 0
    while mySelInt < 1 or mySelInt > _MENU_SIZE:
        mySelInt = int(input("Enter your selection:"))

        if(_DEBUG): print(mySelInt)
        if(mySelInt < 0 and mySelInt > _MENU_SIZE):
            print("Enter a valid menu selection")

    return mySelInt
        


# main entry point
def main():
    mailDict = dict()
    fileName = "mbox-short.txt"
        # process the file
    process_mail_file(fileName, mailDict)

        # loop to display the menu, until the user selects exit
      
    selection = 0
    while selection < _MENU_SIZE:
        selection = displayMenu()
        if(_DEBUG): print("Selection is: ", selection)
        if(selection == 1): print(dictStats(mailDict))
        if(selection == 2): printDict(mailDict)
        if(selection == 3): printDictAlphaSorted(mailDict)
        if(selection == 4): printDictAlphaSorted(mailDict, True)
        if(selection == 5): printDictSendSorted(mailDict)
        if(selection == 6): printDictSendSorted(mailDict, True)
        if(selection == 7): printDictSortedPairs(mailDict)

if __name__=="__main__":
    sys.exit(main())