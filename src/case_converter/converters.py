import re
from enum import Enum

class Case(Enum):
    CAMEL = "camel"
    SNAKE = "snake"
    KEBAB = "kebab"

def getCamelRegex():
    return re.compile("[a-z]+([A-Z][a-z0-9]+)+")

def getSnakeRegex():
    return re.compile("[a-z]+(_[a-z0-9]+)+")

def getKebabRegex():
    return re.compile("[a-z]+(-[a-z0-9]+)+")

def getPascalRegex(): # TODO add support for PascalCase
    return re.compile("([A-Z][a-z0-9_]+)([A-Z][a-z0-9_]+)+")

def getRegex(caseEnum):
    if caseEnum == Case.CAMEL.value:
        return getCamelRegex()
    elif caseEnum == Case.SNAKE.value:
        return getSnakeRegex()
    elif caseEnum == Case.KEBAB.value:
        return getKebabRegex()
    return None

def convertToCamel(inp, out, currCase):
    regex = getRegex(currCase)
    if regex:
        currOut = ""
        for i,line in enumerate(inp):
            match = regex.search(line)
            newLine = line
            while match:
                newId = stringToCamel(match.group(), currCase)
                newLine = newLine[:match.start()]+newId+newLine[match.end():]
                match = regex.search(newLine) # check for another one
            currOut += newLine
        if (out.seekable()): # if out == stdout
            out.seek(0) # if inp == out
            out.truncate()
        out.write(currOut)

def convertToSnake(inp, out, currCase):
    regex = getRegex(currCase)
    if regex:
        currOut = ""
        for i,line in enumerate(inp):
            match = regex.search(line)
            newLine = line
            while match:
                newId = stringToSnake(match.group(), currCase)
                newLine = newLine[:match.start()]+newId+newLine[match.end():]
                match = regex.search(newLine) # check for another one
            currOut += newLine
        if (out.seekable()):
            out.seek(0)
            out.truncate()
        out.write(currOut)

def convertToKebab(inp, out, currCase):
    # TODO
    pass

def stringToCamel(toConvert, currCase):
    out = ""
    if currCase == Case.CAMEL.value:
        out = toConvert
    elif currCase == Case.SNAKE.value:
        makeCap = False
        for char in toConvert:
            if char == '_':
                makeCap = True
            elif makeCap:
                out += char.upper()
                makeCap = False
            else:
                out += char
    elif currCase == Case.KEBAB.value:
        raise NotImplementedError # TODO
    return out

def stringToSnake(toConvert, currCase):
    """
    Converts a single identifier to snake case.
    Depends on the the (regex) definition the cases.
    """
    out = ""
    if currCase == Case.CAMEL.value:
        out += toConvert[0] # I assume toConvert is non-empty
        for char in toConvert[1:]:
            if char.isupper():
                out += '_'+char.lower()
            else:
                out += char
    elif currCase == Case.SNAKE.value:
        out = toConvert
    elif currCase == Case.KEBAB.value:
        out += toConvert[0]
        for char in toConvert[1:]:
            if char.isupper():
                out += '-'+char.lower()
            else:
                out += char
    return out

def stringToKebab(toConvert, currCase):
    # TODO
    pass
