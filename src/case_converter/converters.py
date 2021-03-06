from .regex import *

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
    regex = getRegex(currCase)
    if regex:
        currOut = ""
        for i,line in enumerate(inp):
            match = regex.search(line)
            newLine = line
            while match:
                newId = stringToKebab(match.group(), currCase)
                newLine = newLine[:match.start()]+newId+newLine[match.end():]
                match = regex.search(newLine) # check for another one
            currOut += newLine
        if (out.seekable()):
            out.seek(0)
            out.truncate()
        out.write(currOut)

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
        makeCap = False
        for char in toConvert:
            if char == '-':
                makeCap = True
            elif makeCap:
                out += char.upper()
                makeCap = False
            else:
                out += char
    return out

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
        out = toConvert
    elif currCase == Case.KEBAB.value:
        for char in toConvert:
            if char == '-':
                out += '_'
            else:
                out += char
    return out

def stringToKebab(toConvert, currCase):
    out = ""
    if currCase == Case.CAMEL.value:
        for char in toConvert:
            if char.isupper():
                out += '-' + char.lower()
            else:
                out += char
    elif currCase == Case.SNAKE.value:
        for char in toConvert:
            if char == '_':
                out += '-'
            else:
                out += char
    elif currCase == Case.KEBAB.value:
        out = toConvert
    return out
