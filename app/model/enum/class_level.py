from enum import Enum


class ClassLevel(Enum):
    class Lycee(Enum):
        BAC_SCIENCE
        BAC_MATH
        BAC_TECHNIQUE
        BAC_INFO
        BAC_LETTRE
        TROISIEME_SCIENCE
        TROISIEME_MATH
        TROISIEME_TECHNIQUE
        TROISIEME_INFO
        TROISIEME_LETTRE
        DUEXIEME_MATH
        DUEXIEME_SCIENCE
        DUEXIEME_TECHNIQUE
        DUEXIEME_INFO
        DUEXIEME_LETTRE
        PREMIERE
    class Collegue(Enum):
        SEPTIEME
        HUITIEME
        NEUVIEME
    class Premiere(Enum):
        FIRST
        SECOND
        THIRD
        FOURTH
        FIFTH
        SIXTH
        
