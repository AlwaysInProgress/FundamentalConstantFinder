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

labelMap = dict()

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

def eqOp(target: float, c2: float) -> bool:
    diff = abs(target - c2)
    percent = 1e-10
    if (diff/target < percent):
        return True
    else:
        return False

# OPS = [addOp, mulOp, expOp]
OPS = [mulOp, addOp]

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
    def __init__(self, history: Dict[float, List[str]]):
        self.history = history

    def copy(self):
        return History(copy.deepcopy(self.history))

    def __str__(self):
        if len(self.history) == 0:
            return "No history"
        else:
            return " | ".join(f"{key} = {val}" for key, val in self.history.items())

    def getValueStr(self, val: float) -> str:
        if val in labelMap:
            return str(labelMap[val])
        return str(val)

    def nextExpression(self, val1: float, val2: float, op: str, result: float):
        val1Str = self.findAndRemoveResult(val1) or self.getValueStr(val1)
        val2Str = self.findAndRemoveResult(val2) or self.getValueStr(val2)
        expression = val1Str + op + val2Str
        if result in self.history:
            self.history[result].append(expression)
        else:
            self.history[result] = [expression]

    def findAndRemoveResult(self, result: float) -> Optional[str]:
        for key in self.history:
            if eqOp(key, result):
                val = self.history[result].pop(0)
                if len(self.history[result]) == 0:
                    del self.history[result]
                return f"({val})"
        return None

class Bookkeeper():
    def __init__(self, target: float, consts: List[float], algebraics: List[int], history: History = History({}), foundit: bool = False):
        self.target = target
        self.consts = consts
        self.history = history
        self.foundit = foundit
        self.algebraics = algebraics

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
        return Bookkeeper(self.target, self.consts[:], self.algebraics[:], self.history.copy(), self.foundit)

    def nextGen(self) -> List[Bookkeeper]:
        nextBooks: List[Bookkeeper] = []

        # This is so recursion doesn't continue
        if self.foundit:
            return nextBooks

        # Generate Pairs to check
        pairs: List[Tuple[float, float]] = []
        for i, const1 in enumerate(self.consts):
            for j, const2 in enumerate(self.consts):
                if i != j and const1 < MAX_VAL and const2 < MAX_VAL:
                    pairs.append((const1, const2))

        for pair in pairs: # For each pair, try every possible operation
            for op in OPS:
                # Skip if exp
                if op == expOp:
                    continue

                newVal = op(pair[0], pair[1]) # Perform the operation

                bk = self.copy()

                # Remove old values and replace with new
                bk.consts.remove(pair[0])
                bk.consts.remove(pair[1])
                bk.consts.append(newVal)

                # Add to history
                newHistory = bk.history.copy()
                newHistory.nextExpression(pair[0], pair[1], opToString(op), newVal)
                bk.history = newHistory

                if eqOp(newVal, self.target):
                    # bk contains the correct history
                    bk.foundit = True
                    return [bk]

                nextBooks.append(bk)

        for algebraic in self.algebraics:
            for op in OPS:
                for const in self.consts:
                    newVal = op(const, algebraic)
                    bk = self.copy()
                    bk.consts.remove(const)
                    bk.consts.append(newVal)
                    bk.algebraics.remove(algebraic)

                    # Add to history
                    newHistory = bk.history.copy()
                    newHistory.nextExpression(const, algebraic, opToString(op), newVal)
                    bk.history = newHistory

                    if eqOp(newVal, self.target):
                        # bk contains the correct history
                        bk.foundit = True
                        return [bk]

                    nextBooks.append(bk)

        return nextBooks

def recurse(bk: Bookkeeper) -> Optional[Bookkeeper]:
    print("R: ", bk)
    # Get first two constants, these will be what we op on first
    nextBks = bk.nextGen()
    for nextBk in nextBks:
        if nextBk.foundit:
            return nextBk
        result = recurse(nextBk)
        if result is not None:
            return result
    return None


def nextCase(file):
    # First line are the constants
    consts = [float(x) for x in file.readline().split(",")]
    # Labels for constants
    labels = [x.strip() for x in file.readline().split(",")]

    for index, label in enumerate(labels):
        labelMap[consts[index]] = label

    print("Label Map", labelMap)

    # third line are the algebraics
    algebraics = [int(x) for x in file.readline().split(",")]
    # fourth line is the target
    target = float(file.readline())
    bk = Bookkeeper(target, consts, algebraics)
    startTime = time.perf_counter()

    correctBk = recurse(bk)

    if correctBk is None:
        print("No solution found")
        return

    print("CorrectBk", correctBk.history)
    print("Took", time.perf_counter() - startTime, "seconds")

testFileName = sys.argv[1]
print(testFileName)
with open(testFileName, "r") as file:
    # While there is still data in the file
    while True:
        try:
            nextCase(file)
        except:
            break


