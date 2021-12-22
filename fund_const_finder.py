#!/usr/bin/env python3
from __future__ import annotations
from typing import List, Tuple

# constants
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
class Bookkeeper():
    def __init__(self, target: int, consts: List[int], history: List[Tuple[int, str, int]] = [], foundit: bool = False):
        self.target = target
        self.consts = consts
        self.history = history
        self.foundit = foundit

    def copy(self):
        return Bookkeeper(self.target, self.consts[:], self.history[:], self.foundit)

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
                if op == expOp:
                    if pair[0] > MAX_EXP:
                        continue
                    if pair[1] > MAX_EXP:
                        continue

                newVal = op(pair[0], pair[1]) # Perform the operation
                if newVal == self.target:
                    self.foundit = True

                bk = self.copy()

                # Remove old values and replace with new
                bk.consts.remove(pair[0])
                bk.consts.remove(pair[1])
                bk.consts.append(newVal)
                bk.history.append((pair[0], opToString(op), pair[1]))

                nextBooks.append(bk)

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

def main():
    target = 120
    consts = [1,2,3,4,5,6]
    bk = Bookkeeper(target, consts)
    recurse(bk)

main()

'''
TODO:
-Prune with commutivity of addition/multiplication with flag or something
'''



# 2c + 3


# 1, 2, 3
    # (1 + 2, 3)
    # (1 + 2, 3)
        # a: [0, 5]
        # ((1 + a) + 2, 3)
        # ((1 * a) + 2, 3)
        # ((1 ^ a) + 2, 3)
        # (1 + (2 + a), 3)
        # (1 + (2 * a), 3)
        # (1 + (2 ^ a), 3)
# (1 * 2, 3)

# 1 -> 2
# 1 -> 3
# 1 -> 4


# 2, [1, 2, 3]
    # 3 [2, 3]
        # 5, [3]
            # 8
        # 6, [2]
            # 8
    # 4 [1, 3]
    # 5 [1, 2]


# target = const_dict["c"]

# const_list = np.array(const_list, dtype='float128')
# print(const_list)

# lin_comb_mat = np.array([][])
# operator_mat = np.array([][])
