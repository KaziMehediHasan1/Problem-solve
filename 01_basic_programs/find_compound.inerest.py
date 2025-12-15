# Compound Interest

# funtion
"""def CI(p,t,r):
    A = p * (1 + r/100) ** t
    result = A - p
    return result

result = CI(1200,2,5.4)
print(result)"""

p = 1200
t = 2
r = 5.4

A = p * (pow((1 + r / 100),t))
CI = A - p
print(CI)