# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 09:57:40 2020

@author: Orlando J. Rivera Guevara
@description: Test Environment to identify identifyers:
"""
#Modules used:
import re

#Initializing error_warning
error_warning = ""

print("PHASE 1: IDENTIFY TOKENS\n\n")

#Getting User Input:
user_input = input("CommandLine>")

#Getting my tokens:
tokens = user_input.split()

###############################################################################
#                           Step 1: Identify
###############################################################################

def identifyKeyWords(token):
    if token == "print" or token == "rem" or token == "if" or token == "else" or token == "end":
        return True
    else:
        return False

def isValidIdentifier(token):
    #Accessing Global Variable:
    global error_warning
    
    #Commands used by Command Line:
    #if re.search("cls", token):
    #    os.system('cls')
    #elif re.search("exit", token):
    #    print("Good Bye")
    #    os.system('exit')
    
    if re.search(r'''([0-9])\w+''', token):
        error_warning = "ERROR: Variables cannot start with numbers"
        return False
    elif re.search(r'''\.+\w+\.''', token):
        error_warning = "ERROR: Unexpected function"
        return False
    elif re.search(r'''^\s+$''', token):
        error_warning = "ERROR: Variables cannot contain white spaces"
        return False
    elif re.search(r'''[!@#$%^&*(),.?":{}|<>\/]''', token):
        error_warning = "ERROR: Varibale cannot contain special characters"
        return False
    else: 
        return True

def isArithmeticOperator(token):
    if token == ".add." or token == ".sub." or token == ".mul." or token == ".div.":
        return True
    else:
        return False
    
def isLogicalOperator(token):
    if token == ".or." or token == ".and." or token == ".not." or token == ".eq." or token == ".ne." or token == ".lt." or token == ".le." or token == ".gt." or token == ".ge.":
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
    if re.match(r'^-?\d+(?:\.\d+)?$', token) is None:
        return False
    else:
        return True

for token in tokens:
    if identifyKeyWords(token) is True:
        print("Token is a Keyword: " + token)
    elif isInt(token) is True:
        print("Token is an Int: " + token)
    elif isFloat(token) is True:
        print("Token is a Float: " + token)
    elif isArithmeticOperator(token) is True:
        print("Token is an Arithmetic Operator: " + token)
    elif isLogicalOperator(token) is True:
        print("Token is an Logical Operator: " + token)
    elif isValidIdentifier(token) is True:
        print("Token is a Valid Identifier: " + token)
    else:
        print("Unexpected Error: Cannot Identify this Token: " + token)

###############################################################################
#                           Step 2: Analyze
###############################################################################









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
