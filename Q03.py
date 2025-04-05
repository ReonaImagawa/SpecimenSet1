# -------------------------------------------------------------------
# Import libraries
# -------------------------------------------------------------------

# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------
# ===> Order the jumbled lines
CONCESSION = RETIRED * 2 / 10 * 4
FULL_FARE = 1.50
RETIRED = 2 * STUDENT
STUDENT = 0.25
CHILD = 0.0
# Finished jumbled lines

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
# ===> Choose one line
# layout = "Your fare is {:4.2f}"
# layout = "Your fare is {:4.4f}"

choice = ""
fare = 0.0

# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
def showMenu ():
    print ("----- Fares -----")
    print ("A - Full fare")
    print ("B - Student fare (8 - 16 years)")
    print ("C - Child fare (0 - 7 years)")
    print ("D - Retired (65+ years)")
    print ("E - Other concession")
    print ("Q - Quit")

def getUserChoice ():
    userChoice = ""
    validChoice = False

    # ===> Choose one line
    #while (validChoice):
    #while (not validChoice):
        userChoice = input ("Please choose a fare: ")
        userChoice = userChoice.upper ()
        # ===> Choose one long statement of 3 lines
        #if ((userChoice != "Q") and (userChoice != "A") and
        #        (userChoice != "B") and (userChoice != "C") and
        #        (userChoice != "D") and (userChoice != "E")):
        #if ((userChoice == "Q") or (userChoice == "A") or
        #        (userChoice == "B") or (userChoice == "C") or
        #        (userChoice == "D") or (userChoice == "E")):
            print ("Invalid entry")
        else:
            # Choose one line
            #validChoice = False
            #validChoice = True

    return (userChoice)

def calcFare (pCategory):
    theFare = 0.0

    # ===> Order and indent the jumbled lines
    else:
    elif (pCategory == "C"):
    if (pCategory == "A"):
    elif (pCategory == "B"):
    elif (pCategory == "D"):
    theFare = CONCESSION * FULL_FARE
    theFare = STUDENT * FULL_FARE
    theFare = FULL_FARE
    theFare = CHILD * FULL_FARE
    theFare = RETIRED * FULL_FARE
    # Finished jumbled lines

    return (theFare)

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# ===> Here is a group of jumbled lines
# ===> Order the lines by moving them into their correct location
# ===> Indentation levels are shown for you with commented arrows
# ===> The number of lines to place is shown in brackets after the arrows

#    if (choice != "Q"):
# while (choice != "Q"):
#        print (layout.format (fare))
#    choice = getUserChoice ()
# print ("Goodbye")
#        fare = calcFare (choice)
#    showMenu ()


# ===> (1 line)

    # ===> (3 lines)



        # ===> (2 lines)


# ===> (1 line)

# ----- End of the file -----
