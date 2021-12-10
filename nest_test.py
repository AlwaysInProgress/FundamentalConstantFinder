#!/usr/bin/env python3
import math
import numpy as np


# constants
const_dict = {"c":299792458, "mu_0":12.566370614e-7, "eps_0":8.854187817e-12, "G":6.6740831e-11, "h":6.62607004081e-34,
"e":1.602176620898e-19, "phi_0":2.06783383113e-15, "G_0":7.748091731018e-5, "m_e":9.1093835611e-31, "m_p":1.67262189821e-27,
"m_p/m_e":1836.1526738917, "alpha":7.297352566417e-3, "R_inf":10973731.56850865, "Avogadro":6.02214085774e23,
"F":96485.3328959, "R":8.314459848, "k":1.3806485279e-23, "sigma":5.67036713e-8, "eV":1.602176620898e-19, "u":1.66053904020e-27}

const_list = []
for key in const_dict:
    const_list.append(const_dict[key])

# fundamental functions
def addOp(c1, c2):
    return c1 + c2

def mulOp(c1, c2):
    return c1 * c2

def expOp(c1, c2):
    return c1 ** c2

def nestOp(func1, func2, c1, c2, c3):
    return func1(func2(c1, c2), c3)

# recursive function
def recurse(res, consts, used, target, func, nester = None, nestee = None, third_const = None):
    # print(res, consts, used, target, func.__name__)

    if abs(res - target) < 1e-6:
    # if res == target:
        print("found", used, func.__name__)

    for idx,const in enumerate(consts):
        constCopy = consts[:]
        usedCopy = used[:]
        usedCopy.append(constCopy.pop(idx))

        if func.__name__ == "nestOp" and nester != None and nestee != None and third_const != None:
            recurse(func(nester, nestee, res, const, third_const), constCopy, usedCopy, target, func, nester, nestee, third_const)
        else:
            recurse(func(res, const), constCopy, usedCopy, target, func)

def main():
    ops = [addOp, mulOp, expOp, nestOp]
    nestOps = ops[:-1]

    # constants must not contain 0 or 1
    constants = [2,5,7,2]
    target = 49

    for op in ops:
        for i, const in enumerate(constants):
            for nester_func in nestOps:
                for nestee_func in nestOps:
                    for third_const in constants:
                        remainder = constants[:]
                        remainder.pop(i)
                        recurse(const, remainder, [const], target, op, nester_func, nestee_func, third_const)

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
