# Project: IMPLEMENTATION OF LAO COMPILER
# Version 1.0
# Author: Orlando J. Rivera Guevara
# Date: 12/06/2019

import re

# Setting Error warning:
error_warning = ""


# ##########################################################
#               PHASE 1: Determining Variables:
# ##########################################################

def badVar(variable):
    #Accessing Global Variable:
    global error_warning
    
    if re.search(r'''([0-9])\w+''', variable):
        error_warning = "ERROR: Variables cannot start with numbers"
        return True #bad command so returning True
    elif re.search(r'''^\s+$''', variable):
        error_warning = "ERROR: Variables annot contain white spaces"
        return True #bad command so returning True
    elif re.search(r'''[!@#$%^&*(),.?":{}|<>\/]''',variable):
        error_warning = "ERROR: Varibale cannot contain special characters"
        return True #bad command so returning True
    else: 
        return False #good command so returning False

user_input = str(input('CommandLine>'))


if badVar(user_input) is False:
    print("Good Variable: " + user_input)
elif badVar(user_input) is True:
    print("BAD VARIABLE\n" + error_warning)


# ##########################################################
#               PHASE 2: Compiling Senetences:
# ##########################################################

# Now we determine sentences:

def getCommands(variable):
    result =  re.findall(r'''([^\s]+)''',variable)
    
    #return len(result)
    return result

#print("Words: " + str(getCommands(user_input)))

commands = getCommands(user_input)

#Determining which commands are variables:

for i in range(len(commands)):
    if badVar(commands[i]) is False:
        print(commands[i] + " is good")
    else:
        print(commands[i] + " is bad")
