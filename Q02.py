# -------------------------------------------------------------------
# Import libraries
# -------------------------------------------------------------------
# ===> Fix the syntax error
inport turtle

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
# ===> Fix the NameError
tomasz == turtle.Turtle ()               # Create a turtle
angle = 0
length = 20
key = ""

# ===> Change the name of the variable 'n' to be more meaningful
n = 0

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# ===> Fix the syntax error
tomasz.pencolor "red")
tomasz.pensize (5)

# ===> Add a comment to describe why int() is needed

n = int (input ("Enter number of sides, at least 3: "))

# ===> Calculate angle by dividing 360 by the number of sides and
#      store the value in the variable angle


# ===> Ask the user for the length of each side and store the value
#      in the variable length


for sides in range (n):
  tomasz.forward (length)
  # ===> Fix the logic error
  tomasz.left (70)

key = input ("Press any key")
