import sys
import re

rowCounter = 1
character = ""
    
def lineOutput(line):
    global rowCounter
    global character
    returning = 1
    for char in line.split():
        print(char,"%sxy")
        if char == "//":
            return
        if (len(char)==1):
            returning=1
            if(char=="="):
                character = "OP_PRIDRUZI"
            if(char=="+"):
                character = "OP_PLUS"
            if(char=="-"):
                character = "OP_MINUS"
            if(char=="*"):
                character = "OP_PUTA"
            if(char=="/"):
                character = "OP_DIJELI"
            if(char=="("):
                character = "L_ZAGRADA"
            if(char==")"):
                character = "D_ZAGRADA"
            if (ord(char)>47 and ord(char)<58):
                character = "BROJ"
            if (ord(char)>64 and ord(char)<91) or (ord(char)>96 and ord(char)<123):
                character = "IDN"
        else:
            if (char=="za"):
                character = "KR_ZA"
                returning=1
            elif (char=="od"):
                character = "KR_OD"
                returning=1
            elif (char=="do"):
                character = "KR_DO"
                returning=1
            elif (char=="az"):
                character = "KR_AZ"
                returning=1
            else:
                if ("*" in char) or ("/" in char) or ("+" in char) or ("-" in char) or ("=" in char) or ("(" in char) or (")" in char):
                    charArray = filter(None,re.split('([\(\)=\+-/\*])',char))
                    for char2 in charArray:
                        lineOutput2(char2)
                    returning = 0
                    
                if ((ord(char[0])>64 and ord(char[0])<91) or (ord(char[0])>96 and ord(char[0])<123)):
                    character = "IDN"
                    match = re.match(r"([a-z]+)([0-9]+)([a-z]+)", char, re.I)
                    if match:
                        items = match.groups()
                        for item in items:
                            lineOutput2(item)
                        returning = 0
                        
                else:
                    character = "BROJ"
                    match = re.match(r"([0-9]+)([a-z]+)", char, re.I)
                    if match:
                        items = match.groups()
                        for item in items:
                            lineOutput2(item)
                        returning = 0
                    
        if (returning==1):
            print(str(character) + " " + str(rowCounter) + " " + str(char))

def lineOutput2(char2):
    if (len(char2)==1):
            if(char2=="="):
                character = "OP_PRIDRUZI"
            if(char2=="+"):
                character = "OP_PLUS"
            if(char2=="-"):
                character = "OP_MINUS"
            if(char2=="*"):
                character = "OP_PUTA"
            if(char2=="/"):
                character = "OP_DIJELI"
            if(char2=="("):
                character = "L_ZAGRADA"
            if(char2==")"):
                character = "D_ZAGRADA"
            if (ord(char2)>47 and ord(char2)<58):
                character = "BROJ"
            if (ord(char2)>64 and ord(char2)<91) or (ord(char2)>96 and ord(char2)<123):
                character = "IDN"
    else:
        if (char2=="za"):
            character = "KR_ZA"
        elif (char2=="od"):
            character = "KR_OD"
        elif (char2=="do"):
            character = "KR_DO"
        elif (char2=="az"):
            character = "KR_AZ"
        else:
            if ((ord(char2[0])>64 and ord(char2[0])<91) or (ord(char2[0])>96 and ord(char2[0])<123)):
                character = "IDN"
            else:
                character = "BROJ"
    print(str(character) + " " + str(rowCounter) + " " + str(char2))
    
for line in sys.stdin:
    lineOutput(line)
    rowCounter += 1   
    
