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
