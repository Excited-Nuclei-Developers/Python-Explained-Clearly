# Topic: Sets

# Set is a container data type which holds values from different dtyps or maybe of same datatype.

# properties of Sets:
# 1. Heterogenous elements
# 2. these are generally mutable
# 3. Don't allows duplicates *USP
# 4. unordered and unique

# Operations on sets and how to cerate one

s = {1,2,3,4,5,6,7}
r = {2,4,5,6,7,0,10,9}
print(s, type(s))
print(r, type(r))

# OP1: Intersection
print(s.intersection(r)) # it is going to return us the common values between s and r
# >> 2, 4, 5, 6, 7 

# OP2: Union
print(s.union(r)) # it should return us all the elements from both sets (*only uniques)
# >> 0,1,2,3,4,5,6,7,9,10

# OP3: Difference
print(s.difference(r)) # it should return elemnets of s which are not present in r
# >> 1,3

# OP4: Symmetric difference
print(r.symmetric_difference(s)) # this time we are going to get unique values from both sets
# >> 0,1,3,9,10

name1 = "Shubham"
name2 = "excited nuclei"

s1=set(name1)
s2=set(name2)

print(ord('a'))
print(s1,s2)
print(s1.intersection(s2))