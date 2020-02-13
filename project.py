# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 09:57:40 2020
@author: Orlando J. Rivera Guevara
@description: LAO Interpreter:
"""
#Modules used:
import re

#Initializing error_warning
error_warning = ""

#Getting User Input:
user_input = input("\nCommandLine>")

user_input = user_input.upper()

#Getting my tokens:
tokens = user_input.split()

###############################################################################
#                           Step 1: Identify
###############################################################################
def isString(token):
    if re.search('^"(.*?)"$', token):
        return True
    else:
        return False
def isComment(token):
    if token == "REM":
        return True
    else:
        return False

 
def isKeyWord(token):
    if token == "PRINT" or token == "IF" or token == "ELSE" or token == "END." or token == "THEN":
        return True
    else:
        return False

def isValidIdentifier(token):
    #Accessing Global Variable:
    global error_warning
   
    if re.search(r'''([0-9])\w+''', token):
        error_warning = "ERROR: Variables cannot start with numbers: " + token
        return False
    elif re.search(r'''\.+\w+\.''', token):
        error_warning = "ERROR: Valid String: " + token
        return False
    elif re.search(r'''cld''', token):
        error_warning = "ERROR: Variables cannot contain white spaces: " + token
        return False
    elif re.search(r'''[!@#$%^&*(),.?":{}|<>\/]''', token):
        error_warning = "ERROR: Varibale cannot contain special characters: " + token
        return False
    else:
        return True

def isArithmeticOperator(token):
    if token == ".add." or token == ".ADD." or token == ".sub." or token == ".SUB." or token == ".mul." or token == ".MUL." or token == ".div." or token == ".DIV.":
        return True
    else:
        return False
   
def isLogicalOperator(token):
    if token == ".OR."or token == ".AND." or token == ".AND." or token == ".EQ." or token == ".NE." or token == ".LT." or token == ".LE." or token == ".GT." or token == ".GE.":
        return True
    else:
        return False

#Only detects positive integers:
def isInt(token):
    if token.isdigit():
        return True
    else:
        return False

def isFloat(token):
    if re.match(r'^(\+|\-)\d+(?:\.\d+)?$', token) is None:
        return False
    else:
        return True
def isAssignmentOperator(token):
    if token == r"=":
        return True
    else:
        return False

#Loops through token list to validate tokens:
def isTokenErrorFree(list):
    
    for token in tokens:
        if isArithmeticOperator(token):
            next
        elif isAssignmentOperator(token):
            next
        elif isInt(token):
            next
        elif isValidIdentifier(token):
            next
        elif isString(token):
            next
        elif isKeyWord(token):
            next
        elif isLogicalOperator(token):
            next
        elif isFloat(token):
            next
        else:
            input("ERROR Unidentified Token: " + token)
            exit()
    return True

###############################################################################
#                           Step 2: Analyze
###############################################################################

#Defining if tokens are compatible:

#What makes a token compatible?
#Certain tokens can be next to each other and execute but other tokens cannot
#Start by going over all the errors and documenting them.

#Error 1: Incompatible Print Statement
'''
Print statement cannot be followed by:
- A keyword
- An arithmetic
- A Logical operator
- An assignment operator
'''

def isSentenceErrorFree(list):
    
    for i in range(len(list)):
        
        if i > 0:
            if isKeyWord(list[i - 1]) is True and (isKeyWord(list[i]) is True or isAssignmentOperator(list[i]) is True or isArithmeticOperator(list[i]) is True or isLogicalOperator(tokens[i]) is True):
                input("Error, Keyword out of place")
                exit()
            elif isArithmeticOperator(list[i - 1]) is True and (isKeyWord(list[i]) is True or isAssignmentOperator(list[i]) is True or isArithmeticOperator(list[i]) is True or isLogicalOperator(list[i]) is True):
                input("Error, Arithmetic Operator out of place")
                exit()
            elif isLogicalOperator(list[i - 1]) is True and (isKeyWord(list[i]) is True or isAssignmentOperator(list[i]) is True or isArithmeticOperator(list[i]) is True or isLogicalOperator(list[i]) is True):
                input("Error, Logical Operator out of place")
                exit()
            elif isAssignmentOperator(list[i - 1]) is True and (isKeyWord(list[i]) is True or isAssignmentOperator(list[i]) is True or isArithmeticOperator(list[i]) is True or isLogicalOperator(list[i]) is True):
                input("Error, Amssignment Operator out of place")
                exit()
    return True

###############################################################################
#                           Step 3: Execute
###############################################################################
if isTokenErrorFree(tokens) is True and isSentenceErrorFree(tokens) is True:
    commands = open("commands.txt", "w")
execute(commands.txt)
