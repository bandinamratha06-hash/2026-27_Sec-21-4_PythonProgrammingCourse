# Program to demonstrate Operator Precedence and Associativity
a=int(input("enter a num1"))
b=int(input("enter a num2"))
c=int(input("enter a num3"))
# Operator precedence
result1 =a+(b*c)
print("result1 =", result1)
# Parentheses have higher precedence
result2 = (a+b)*c
print("result2 =", result2)
# Operator associativity
result3 =a-b-c
print("result3=", result3)
# Exponentiation is right-associative
result4 = a**b**c
print("result4 =", result4)
