"""models
supporting classes and structs"""
from enum import Enum

class Symbol(str, Enum):
    X = "X"
    O = "O"
    