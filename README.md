# Fundamental Constants

We want a way to loop over all possible functions and apply all fundamental constants to them in order to find new relations.

cn is a fundamental constant

1. c1 = c2 + a, where n is an algebraic number
2. c1 = sum(cn), where cn is any subset of our constants
   2.5. c1 = a \* c2
3. c1 = prod(cn,a), where n is an algebraic number
4. c1 = prod(cn^a, b), where cn is any subset of our constants and a is an algebraic number
5. c1 = sum(prod(cn^a, b)), where cn is any subset of our constants and a is an algebraic number

5 = 2 -> 4

Ops

1. F(c1, c2) = c1 + c2 => [c1,c2] \* [1,1]' = c1 + c2
2. F(c1, c2) = c1 _ c2 => [c1,c2] _ [c2 /2 , c1 /2]'
3. F(c) = c + a
4. F(c) = c \* a
5. F(c) = c ^ a

c1 = c2 + c3 \* c4 === F2(c2, F3(c3, c4))

F([A,B,C], [ c2, c3, c3 ]) => A _ c2 _ c3 _ c4 + B _ c2 ^2 \* + ...

Some function f that given 2 num => all possible combinations of ops

F(c_1, c_2) = c_3

c1 = n1 _ c_k ^ a1 _ c_k1 ^ a2

2e^2/2πh

c_1 is a linear combination of (c_2, ...,c_n) = c_1 \* an nx1 vector

OP = (c*2, ...,c_n)\_matrix*(c_2, ...,c_n)^T

OP([[A, B],[C, D]]) = Ax^2 + (B+C)xy + Dy^2

c_1 = c_2 ^ n / c_3 ^ n - 1

[((1, '+', 2), '+', 3),(4, '*', 5), (6, '*', 6), (20, '*', 36)]
[(((4, '*', 5), '*', ((1, '+', 2), '+', 3), '*', 6))]

BK { const = [1,2,3,4,5,6], history = []}
BK { const = [3,3,4,5,6], history = [(1,'+',2)]}
BK { const = [6,4,5,6], history = [(1,'+',2), (3 + 3)]}

BK { const = [1,2,3,4,5,6], history = []}
if not find NEW_RESULT in history
VAL1 = 1
VAL2 = 2
RESULT = 3
return [..., (VAL1 OP VAL2, RESULT)]
BK { const = [3,3,4,5,6], history = [("1+2",3)]}
VAL1 = 3 -> "1+2"
VAL2 = 3
OP="+"
RESULT=6
OLD_STR="1+2"
OLD_RESULt=3
return ("(LAST) OP LAST_RESULT", NEW_RESULT)
BK { const = [6,4,5,6], history = ("(1+2)+3", 6)]}
if not find NEW_RESULT in history
VAL1 = 4
VAL2 = 5
RESULT = 20
return [..., (VAL1 OP VAL2, RESULT)]
BK { const = [20,6,6], history = [("(1+2)+3",6), ("4*5",20)]}
BK { const = [20, 36], history = ("((1+2)+3)\*6",36), ("4*5",20)}
VAL1=20
VAL2=36
OP="*"
RESULT=720

[("(((1+2)+3)*6)*20", 720), ("4*5", 20)]

BK { const = [720], history = ("(((1+2)+3)\*6)\*(4\*5) }

pseudocode pretty print (BK, op, val1, val2, result):
val1Str = "(BK.history.findAndRemoveResult(val1))" || "val1"
val2Str = "(BK.history.findAndRemoveResult(val2))" || "val2"
return [...BK.history, ("val1Str op val2Str", result)]

1.  val1Str = "((1+2)+3)\*6"
    history = [("4*5",20)]
2.  val2Str="4\*5"
    history = []
3.  return ["(((1+2)+3)\*6)\*(4\*5)"]

BK { const = [20,6,6], history = [("(1+2)+3",6), ("4*5",20)]}
VAL1=6
VAL2=6
OP="\*"

1. val1str = "(1+2)+3"
   history = [("4*5",20)]
2. val2 = "6"
   history = [("4*5",20)]
   return [("4\*5",20), ("((1+2)+3)*6", 36)]

- given val1, val2, op, history containing all previous operations in parallel
- val1str = string corresponding to result if in history, else "val1"
- remove element from history
- val2str = string corresponding to result if in history, else "val2"
- remove element from history
- append "val1str op val2str" to history
- return history

{3: ["1+2"]}
