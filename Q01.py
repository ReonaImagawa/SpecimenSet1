# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------
MAX_BOXES = 5

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
boxes = ["circle", "square", "triangle", "hexagon", "octagon"]

# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
def isValid (pLocation):
    valid = False

    if (pLocation - 1 >= 0) and (pLocation - 1 < MAX_BOXES):
        valid = True
    return (valid)

def showBox (pLocation):
    theString = ""

    theString = "The box is " + boxes[pLocation - 1] + " shaped."
    print (theString)

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
choice = int (input ("Welcome to the game.  Choose a number (1 to 5)"))
if (isValid (choice)):
    showBox (choice)
else:
    print ("Invalid choice")

# -------------------------------------------------------------------
# =====> Write your answers here in the right hand column
# Left Column                                   # Right Column
# -------------------------------------------------------------------
# Give the name of a parameter                  #
# Give the symbol used to show assignment       #
# Give the name of a structured data type implemented as a list
                                                #
# Give the name of a built-in subprogram        #
# Give the name of a user-devised function      #
# Give the name of a constant                   #
# Give the name of a local variable             #
