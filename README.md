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
