# type casting in python

# what is type casting?

a=1
b=2.34
c="Shubham"
d=True
e=1+4j
f=[1,2,3,4]

# print(f'dtype of a is :{type(a)}')
# print(f'dtype of b is :{type(b)}')
# print(f'dtype of c is :{type(c)}')
# print(f'dtype of d is :{type(d)}')
# print(f'dtype of e is :{type(e)}')
# print(f'dtype of f is :{type(f)}')

a_fl=float(a)
b_fl=float(b)
# c_fl=float(c) # can't convert string to float
d_fl=float(d)
# e_fl=float(e) # complex cant be converted to float 
# f_fl=float(f) # container dtypes can't be converted to float

print(f'dtype of a is :{a_fl,type(a_fl)}')
print(f'dtype of b is :{b_fl,type(b_fl)}')
# print(f'dtype of c is :{type(c_fl)}')
print(f'dtype of d is :{d_fl,type(d_fl)}')
# print(f'dtype of e is :{type(e_fl)}')
# print(f'dtype of f is :{type(f_fl)}')

# to summarize 
# numeric dtypes can be converted to numeric and string dtypes 
# (bec; string conatins alpha numeric characters)

# strings can't be converted to other dtypes

# complexes cant be converted into other dtypes

# container dtypes can only be converted to container type only 
# with certain conditions only