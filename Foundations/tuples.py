# Topic: Tuples
# these are actually also a container datatype. similar to lists.

# that tuples are actually non-mutable. this shows the difference between tuples and lists.

t=(1,)
print(type(t),len(t))
print(id(t))
# t tuple id >> 2391571922128
t += (2,)
print(t, len(t), id(t))
# t tuple id >> 2934820758784

# accessesing the values of tuples

t += (1,11,3,5,44,3,2,6)
print(t)

print(t[2::2]) # it is going to fetch me the values at even indexes (2,4,6,8,....,len(tuple)//2)

# sorting of tuple
# using inbuilt function
sorted_t = sorted(t)
print(sorted_t)

# l = [1, 2, 1, 11, 3, 5, 44, 3, 2, 6]
# l.sort()
# print(l)