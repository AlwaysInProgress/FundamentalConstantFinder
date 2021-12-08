#!/usr/bin/env python3
import math
import numpy as np

const_dict = {"c":299792458, "mu_0":12.566370614e-7, "eps_0":8.854187817e-12, "G":6.6740831e-11, "h":6.62607004081e-34,
"e":1.602176620898e-19, "phi_0":2.06783383113e-15, "G_0":7.748091731018e-5, "m_e":9.1093835611e-31, "m_p":1.67262189821e-27,
"m_p/m_e":1836.1526738917, "alpha":7.297352566417e-3, "R_inf":10973731.56850865, "Avogadro":6.02214085774e23,
"F":96485.3328959, "R":8.314459848, "k":1.3806485279e-23, "sigma":5.67036713e-8, "eV":1.602176620898e-19, "u":1.66053904020e-27}

const_list = []
for key in const_dict:
    const_list.append(const_dict[key])


def addOp(c1, c2):
    return c1 + c2

def mulOp(c1, c2):
    return c1 * c2

def expOp(c1, c2):
    return c1 ** c2



def recurse(func, sum, consts, used, target):
    if sum == target:
        print("found", used)

    for idx,const in enumerate(consts):
        copy = consts[:]
        usedCopy = used[:]
        usedCopy.append(copy.pop(idx))
        recurse(func, func(sum, const), copy, usedCopy, target)

def main():
    ops = [
        (mulOp, 1),
        (addOp, 0)
    ]

    for op, starting in ops:
        recurse(op, starting, [1,2,3], [], 6)

main()



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
