import re
from enum import Enum

class Case(Enum):
    CAMEL = "camel"
    SNAKE = "snake"
    KEBAB = "kebab"

def getCamelRegex():
    return re.compile("[a-z_]+([A-Z][a-z0-9_]+)+|([A-Z][a-z0-9_]+)([A-Z][a-z0-9_]+)+")

def getSnakeRegex():
    # TODO
    return re.compile()

def getKebabRegex():
    # TODO
    return re.compile()

def getRegex(caseEnum):
    if caseEnum == Case.CAMEL.value:
        return getCamelRegex()
    elif caseEnum == Case.SNAKE.value:
        return getSnakeRegex()
    elif caseEnum == Case.KEBAB.value:
        return getKebabRegex()
    return None

def convertToCamel(inp, out, currCase):
    # TODO
    pass

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
        out.write(currOut)

def convertToKebab(inp, out, currCase):
    # TODO
    pass

def stringToSnake(toConvert, currCase):
    """
    Converts a single identifier to snake case.
    Depends on the the (regex) definition the cases.
    """
    out = ""
    if currCase == Case.CAMEL.value:
        for char in toConvert:
            if char.isupper():
                out += '_'+char.lower()
            else:
                out += char
    elif currCase == Case.SNAKE.value:
        raise NotImplementedError # TODO
    elif currCase == Case.KEBAB.value:
        raise NotImplementedError # TODO
    return out
