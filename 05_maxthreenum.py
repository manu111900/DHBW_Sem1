###############################################################################################
# Dateiname:    05_maxthreenum.py  [1-5]                                                      #
# ------------------------------------------------------------------------------------------- #
# Implement.:   https://www.programiz.com/python-programming/examples/largest-number-three    #
# Algorithmus:  Maximum3.pdf                                                                  #
# Ein-/Ausgabe: num1=10,num2=14,num3=12 / largest=14                                          #
# Beschreibung: Max. dreier ganzen Zahlen                                                     #
# Lernziele:    Bedingte Anweisung / Verzweigung (if .. elif .. else)                         #
# Anmerkungen:                                                                                #
###############################################################################################

# fixed values of num1, num2 and num3
# num1 = 10
# num2 = 14
# num3 = 12

# or values taken from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Calculation
# Exakte Umsetzung
if (num1 >= num2):
    if (num3 >= num1):
       largest = num3
    else:
       largest = num1
elif (num3 >= num2):
    largest = num3
else:
    largest = num2

"""
Alternative 1:

if (num1 >= num2):
    if (num3 >= num1):
        largest = num3
    else:
        largest = num1
else:
    if (num3 >= num2):
        largest = num3
    else:
        largest = num2

Alternative 2 ('freie Interpretation'):

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
"""

# f-string formatting
print(f"The largest number between {num1}, {num2} and {num3} is {largest}.")

# Slightly older formatting, note that 'd' in '{0:d} etc. can be omitted, see https://pyformat.info/#simple
# print("The largest number between {0:d}, {1:d} and {2:d} is {3:d}".format(num1, num2, num3, largest))

# No formatting
# print("The largest number between",num1,",",num2,"and",num3,"is",largest)