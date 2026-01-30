# Que : Why does 5+2 work, but "5"+2 doesn't?
print(5+2)
# print('5'+2)

# Arithematic Operators
a=2
b=3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)

# How same operators works differently with different dtype?
s1='Welcome, to'
s2='Excited Nuclei channel'
print(s1+s2)
# print(s1-s2)
print(s1*2)
# print(s1*s2)
print('5'+'2')

# Comparison Operators with Example
print(a<b) # 2<3 >> true 
print(a>b)
print(a==b)
print(a!=b)

if a<b:
    print('a is greater than b')

# Logical Operators
age=20
has_lic=True

print(age>18 and has_lic) # and checks for both statements to be true
print(age<18 or has_lic) # it checks that atleast one is true
print(not has_lic)

# Assignment Operators
print("value of a is ",a)
a+=1 # a=a+1
a//=1
a*=1
a-=1
# some more 
print(a)

if a==1:
    print('True')

# write a program that checks for a number to be even and greater than 10.