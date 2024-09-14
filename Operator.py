'''Aeithmetic Operator'''
a = 2
b = 79

print(a+b)
print(a-b)
print(a*b)
print(b/a)
"""Reminder"""
print(b%a)
"""a^b"""
print(b**a)

'''Relational or conditional operator'''

"""Equals to"""
print(a==b)
'''not equals to'''
print(a!=b)
print(a>=b)
print(b>a)
print(b<=a)
print(b<a)

'''Assignment operator'''

num = 100
num *= 7
print("num: ", num)
num /= 2
print("num: ", num)
num+= 100
print("num: ", num)
num-=20
print("num: ", num)
num%=7
print("num: ", num)
num**=3
print("num: ", num)

'''Logical Operator'''
'''Not operator'''
sales=6000
profit=300
print(not False)
print(not True)
print(not profit>sales)

Value1 =True
Value2 =False
print("and operator: ", Value1 and Value2)
print("or operator: ", Value1 or Value2)

"""Condition Rules
and : TT=T, TF=F, FT=F, FF=F
Or : TT=T, TF=T, FT=T, FF=F"""
w=2
x=3
print("or operator: ", (w==x) or (w>x))

a=input("number1: ")
b=input("number2: ")
a=float(a)
b=float(b)
sum=(a+b)
print(sum)