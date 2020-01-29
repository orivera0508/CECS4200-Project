# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 09:57:40 2020

@author: Orlando J. Rivera Guevara
@description: Test Environment to identify tokens:
"""
#Modules used:
import re

#Initializing error_warning
error_warning = ""

print("PHASE 1: IDENTIFY TOKENS\n\n")

#Getting User Input:
user_input = input("CommandLine>")

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
   
def isKeyWord(token):
    if token == "print" or token == "PRINT" or token == "rem" or token == "REM" or token == "if" or token == "IF" or token == "else" or token == "ELSE" or token == "end." or token == "END." or token == "THEN" or token == "then":
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
    if token == ".or." or token == ".OR." or token == ".and." or token == ".AND." or token == ".not." or token == ".AND." or token == ".eq." or token == ".EQ." or token == ".ne." or token == ".NE." or token == ".lt." or token == ".LT." or token == ".le." or token == ".LE." or token == ".gt." or token == ".GT." or token == ".ge." or token == ".GE.":
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

'''
for token in tokens:
    if isString(token) is True:
        print("Token is a valid string: " + token)
    elif identifyKeyWords(token) is True:
        print("Token is a Keyword: " + token)
    elif isInt(token) is True:
        print("Token is an Unsigned Int: " + token)
    elif isFloat(token) is True:
        print("Token is a real: " + token)
    elif isArithmeticOperator(token) is True:
        print("Token is an Arithmetic Operator: " + token)
    elif isLogicalOperator(token) is True:
        print("Token is an Logical Operator: " + token)
    elif isValidIdentifier(token) is True:
        #A-F: int, G-N: real, O-Z: string
        if re.search(r'^[A-Fa-f].*$', token):
            print("Token is a Valid Identifier (int): " + token)
        elif re.search(r'^[G-Ng-n].*$', token):
            print("Token is a Valid Identifier (real): " + token)
        elif re.search(r'^[O-Zo-z].*$', token):
            print("Token is a Valid Identifier (string): " + token)
    else:
        if error_warning is None:
            print("Unexpected Error: Cannot Identify this Token: " + token)
        else:
            print(error_warning)
'''
###############################################################################
#                           Step 2: Analyze
###############################################################################

def ifCompatible(list):
    #Testing token validity:
    for j in range(len(list)):
            if isString(list[j]) is True or isKeyWord(list[j]) is True or isValidIdentifier(list[j]) is True or isArithmeticOperator(list[j]) is True or isLogicalOperator(list[j]) is True or isInt(list[j]) is True or isFloat(list[j]) is True:
                next
            else:
                print("ERROR: Invalid token: " + list[j])
                input("PROGRAM EXITED WITH ERROR CODE: " + str(0) + "\nPRESS ANY KEY TO CONTINUE")
                exit()
   
    #Sequences that will work:
    for i in range(len(list)):

        #Testing if expressions are valid:
        if isKeyWord(list[i]) is True:
            if list[0] == "REM":
                print("Valid REM Statement: " , end = "")
                print(*list)
                return True
                break
            elif list[i] == "PRINT":
                if isKeyWord(list[i + 1]) is True or isArithmeticOperator(list[i + 1]) is True or isLogicalOperator(list[i + 1]) is True or isAssignmentOperator(list[i + 1]) is True:
                    print("INVALID PRINT STATEMENT: ", end = "")
                    print(*list)
                    input("PROGRAM EXITED WITH ERROR CODE: " + str(1) + "\nPRESS ANY KEY TO CONTINUE")
                    exit()
                elif isInt(list[i + 1]) is True or isFloat(list[i + 1]) is True or isValidIdentifier(list[i + 1]) is True or isString(list[i + 1]) is True:
                    #print("VALID PRINT STATEMENT: ", end = "")
                    #print(*list)
                    next
            elif list[i] == "IF":
                if isKeyWord(list[i + 1]) is True or isArithmeticOperator(list[i + 1]) is True or isLogicalOperator(list[i + 1]) is True or isAssignmentOperator(list[i + 1]) is True:
                    print("INVALID IF STATEMENT: ", end = "")
                    print(*list)
                    input("PROGRAM EXITED WITH ERROR CODE: " + str(2) + "\nPRESS ANY KEY TO CONTINUE")
                    exit()
                if isInt(list[i + 1]) is True or isFloat(list[i + 1]) is True or isValidIdentifier(list[i + 1]) is True or isString(list[i + 1]) is True:
                    #print("VALID PRINT STATEMENT: ", end = "")
                    #print(*list)
                    next
            elif list[i] == "THEN":
                if isKeyWord(list[i + 1]) is True or isArithmeticOperator(list[i + 1]) is True or isLogicalOperator(list[i + 1]) is True or isAssignmentOperator(list[i + 1]) is True:
                    print("INVALID THEN STATEMENT: ", end = "")
                    print(*list)
                    input("PROGRAM EXITED WITH ERROR CODE: " + str(3) + "\nPRESS ANY KEY TO CONTINUE")
                    exit()
                if isInt(list[i + 1]) is True or isFloat(list[i + 1]) is True or isValidIdentifier(list[i + 1]) is True or isString(list[i + 1]) is True:
                    #print("VALID PRINT STATEMENT: ", end = "")
                    #print(*list)
                    next
            elif list[i] == "END.":
                if isKeyWord(list [i + 1]) is True or isArithmeticOperator(list[i + 1]) is True or isLogicalOperator(list[i + 1]) is True or isAssignmentOperator(list[i + 1]) is True or isInt(list[i + 1]) is True or isFloat(list[i + 1]) is True or isValidIdentifier(list[i + 1]) is True or isString(list[i + 1]) is True:
                    print("INVALID END. STATEMENT: ", end = "")
                    print(*list)
                    input("PROGRAM EXITED WITH ERROR CODE: " + str(4) + "\nPRESS ANY KEY TO CONTINUE")
                    exit()
                   
        if isString(list[i]) is True:
            if isAssignmentOperator(list[i - 1]) is False or (isKeyWord(list[i - 1]) is False and (list[i - 1] != "PRINT" or list[i - 1] != "REM")):
                 print("INVALID STATEMENT, STRING AT BEGGINING OF CODE: ", end = "")
                 print(*list)
                 input("PROGRAM EXITED WITH ERROR CODE: " + str(5) + "\nPRESS ANY KEY TO CONTINUE")
                 exit()
            elif isKeyWord(list[i + 1]) is True or isArithmeticOperator(list[i + 1]) is True or isLogicalOperator(list[i + 1]) is True or isAssignmentOperator(list[i + 1]) or True or isInt(list[i + 1]) is True or isFloat(list[i + 1]) is True or isValidIdentifier(list[i + 1]) is True or isString(list[i + 1]) is True:
                next
		
		if isValidIdentifier(list[i]) is True:
			if isValidIdentifier(list[i + 1]) is True or isValidIdentifier(list[i - 1]) is True or isString(list[i + 1]) is True or isString(list[i - 1]) is True:
				print("INVALID STATEMENT, VARIABLE AMBIGUITY: ", end = "")
				print(*list)
				input("PROGRAM EXITED WITH ERROR CODE: " + str(6) + "\nPRESS ANY KEY TO CONTINUE")
				exit()
				
ifCompatible(tokens)


###############################################################################
#                           Step 3: Execute
###############################################################################
'''
def lexicalAnalysis(list):
    #print(list)
   
    for i in range(len(list)):
    #Things that will prompt an error during lexical analysis:
        if isArithmeticOperator(list[0]) is True or isLogicalOperator(list[0]) is True:
            print(list[0])
            print("ERROR: Invalid Syntax")
            break
     #This is my print statement:
        elif identifyKeyWords(list[i]) is True and list[i] == "print" and '"' in list[i + 1]:
            sentence = ""
            for i in list[i + 1:]:
                sentence =sentence + i.replace('"', '') + " "
            print (sentence)

lexicalAnalysis(tokens)
'''
