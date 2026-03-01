# Topic: List

# what are lists ?
# it is a container data type that stores multiple values

# how to create a list ?

l=[]
print(type(l))

# Properties of lists :
# 1. hetrogenous
# 2. mutable
# 3. can contains duplicates 
# 4. elements are seprated by ","

# hetrogenous means can contain different dtypes 
l1 = [1, 2.23, True, 2+3j, "Excited Nuclei"]
# print(l1)

# mutability of lists means the lists can be changed and updated after the creation.

# basic operation on lists

# 1. adding an element to it
print(f"List: {l1}, id of this list is: {id(l1)}")
l1.append("Python explained clearly.") # add obj to end of list
print(f"List: {l1}, id of this list is: {id(l1)}")

# insert and extend >> try your own

# 2. joining 2 lists
l=[1,23]
print(l1+l)

# 3. finding features like min, max, len, etc
print(len(l1))
# Note : when using functions like 
# min, max, mean, mode, median, and 
# sorted/ sort list must be homogenus

# try sorting and finding the min and max from the list = ['a','b','c','d']

# 4. in and not in
print(2 in l1)