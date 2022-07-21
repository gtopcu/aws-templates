
#   Operator	            Description	                        Example
#   +, -	                Addition, Subtraction	            10 - 3
#   *                       Multiplication                      2 * 2
#   **                      Power                               2 ** 3 = 8
#   /                       Natural divide(float)               3 / 2 = 1.5
#   //                      Floor divide(int)                   3 / 2 = 1
#   %	                    Modulo	                            27 % 7 = 6
#   <, <=, >, >=, !=, ==	The usual comparison operators

print(3 / 2)
print(3 // 2)
print(2 ** 3)
print(19 % 3)


#   /	Division
#   This operation brings about different results for Python 2.x (like floor division) and Python 3.x	Python3:
#   10  / 3
#   3.3333333333333335

#   //	Truncation Division (also known as floordivision or floor division)
#   The result of this division is the integral part of the result, i.e. the fractional part is truncated, 
#   if there is any.
#   It works both for integers and floating-point numbers, but there is a difference between the type of the 
#   results: If both the dividend and the divisor are integers, the result will also be an integer. 
#   If either the divident or the divisor is a float, the result will be the truncated result as a float.	
#   10 // 3
#   3
#   If at least one of the operands is a float value, we get a truncated float value as the result.
#   10.0 // 3
#   3.0
#
#   A note about efficiency:
#   The results of int(10 / 3) and 10 // 3 are equal. But the "//" division is more than two times as fast! 
#   You can see this here:

#In [9]: %%timeit
for x in range(1, 100):
    y = int(100 / x)
#100000 loops, best of 3: 11.1 μs per loop
#In [10]: %%timeit
for x in range(1, 100):
    y = 100 // x
#100000 loops, best of 3: 4.48 μs per loop


#   +x, -x	Unary minus and Unary plus (Algebraic signs)	-3
#   ~x	Bitwise negation	~3 - 4 Result: -8
#  **	Exponentiation	10 ** 3 Result: 1000
#   or, and, not	Boolean Or, Boolean And, Boolean Not	(a or b) and c
#   in	"Element of" 1 in [3, 2, 1]
#   <, ≤, >, ≥, !=, ==	The usual comparison operators	2 ≤ 3
#   |, &, ^	Bitwise Or, Bitwise And, Bitwise XOR	6 ^ 3
#   <, >	Shift Operators	6 < 3