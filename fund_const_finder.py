#!/usr/bin/env python3
from __future__ import annotations
from typing import List, Tuple, Dict, Optional
import time
import sys
import copy


const_dict = {"c":299792458, "mu_0":12.566370614e-7, "eps_0":8.854187817e-12, "G":6.6740831e-11, "h":6.62607004081e-34,
"e":1.602176620898e-19, "phi_0":2.06783383113e-15, "G_0":7.748091731018e-5, "m_e":9.1093835611e-31, "m_p":1.67262189821e-27,
"m_p/m_e":1836.1526738917, "alpha":7.297352566417e-3, "R_inf":10973731.56850865, "Avogadro":6.02214085774e23,
"F":96485.3328959, "R":8.314459848, "k":1.3806485279e-23, "sigma":5.67036713e-8, "eV":1.602176620898e-19, "u":1.66053904020e-27}

const_list = []
for key in const_dict:
    const_list.append(const_dict[key])

MAX_VAL = 2**64
MAX_EXP = 11

# fundamental functions
def addOp(c1, c2):
    return c1 + c2

def mulOp(c1, c2):
    return c1 * c2

def expOp(c1, c2):
    return c1 ** c2

OPS = [addOp, mulOp, expOp]

def opToString(op) -> str:
    if op == addOp:
        return "+"
    elif op == mulOp:
        return "*"
    elif op == expOp:
        return "^"
    else:
        return "?"

class History():
    def __init__(self, history: Dict[int, List[str]]):
        self.history = history

    def copy(self):
        return History(copy.deepcopy(self.history))

    def __str__(self):
        for key in self.history:
            print(key, ":", self.history[key][0])

    def nextExpression(self, val1: int, val2: int, op: str, result: int) -> str:
        val1Str = self.findAndRemoveResult(val1) or str(val1)
        val2Str = self.findAndRemoveResult(val2) or str(val2)
        expression = val1Str + op + val2Str
        if result in self.history:
            self.history[result].append(expression)
        else:
            self.history[result] = [expression]

    def findAndRemoveResult(self, result: int) -> Optional[str]:
        if result in self.history:
            val = self.history[result].pop(0)
            if len(self.history[result]) == 0:
                del self.history[result]
            return f"({val})"
        return None

class Bookkeeper():
    def __init__(self, target: int, consts: List[int], history: History = History({}), foundit: bool = False):
        self.target = target
        self.consts = consts
        self.history = history
        self.foundit = foundit

    def __repr__(self):
        return "Consts: %s Hist: %s" % (self.consts, self.history)

    def __eq__(self, other):
        if isinstance(other, Bookkeeper):
            # check if both arrays contain the same values
            for item in self.consts:
                if item not in other.consts:
                    return False
            for item in other.consts:
                if item not in self.consts:
                    return False
            return True
        else:
            return False

    def __ne__(self, other):
        return (not self.__eq__(other))

    def __hash__(self):
        return hash(self.__repr__())

    def copy(self):
        return Bookkeeper(self.target, self.consts[:], self.history.copy(), self.foundit)

    def nextGen(self) -> List[Bookkeeper]:
        nextBooks: List[Bookkeeper] = []

        if self.foundit:
            return nextBooks

        # Generate Pairs to check
        pairs: List[Tuple[int, int]] = []
        for i, const1 in enumerate(self.consts):
            for j, const2 in enumerate(self.consts):
                if i != j and const1 < MAX_VAL and const2 < MAX_VAL:
                    pairs.append((const1, const2))

        for pair in pairs: # For each pair, try every possible operation
            for op in OPS:

                # Skip if exp is too large
                if op == expOp and pair[1] > MAX_EXP:
                    continue

                newVal = op(pair[0], pair[1]) # Perform the operation

                if newVal == self.target:
                    self.foundit = True

                bk = self.copy()

                # Remove old values and replace with new
                bk.consts.remove(pair[0])
                bk.consts.remove(pair[1])
                bk.consts.append(newVal)

                # Add to history
                newHistory = bk.history.copy()
                newHistory.nextExpression(pair[0], pair[1], opToString(op), newVal)
                bk.history = newHistory

                nextBooks.append(bk)

        # Add 2



        # Remove duplicates
        # nextBooks = list(set(nextBooks))
        return nextBooks

def recurse(bookKeeper: Bookkeeper):
    if (bookKeeper.foundit):
        print("Found it!", bookKeeper.history, " = ", bookKeeper.target)
        return True
    # Get first two constants, these will be what we op on first
    nextBks = bookKeeper.nextGen()
    for bk in nextBks:
        if (recurse(bk)):
            return True
    return False


def nextCase(file):
    # First line are the constants
    consts = [int(x) for x in file.readline().split(",")]
    # second line is the target
    target = int(file.readline())
    bk = Bookkeeper(target, consts)
    startTime = time.perf_counter()
    recurse(bk)
    print("Took", time.perf_counter() - startTime, "seconds")
    print(bk.history)

testFileName = sys.argv[1]
print(testFileName)
with open(testFileName, "r") as file:
    # While there is still data in the file
    while True:
        try:
            nextCase(file)
        except:
            break


