# Topic: Dictionaries
# Key value pairs that used to store data in structured format.

# Sp. Condn: the keys must be hashable
# datatypes that are immutable are generally hashable 
# eg: strings, tuples, numbers

# values can be either container dtype or it can be a single element.

# creating dictionary {Keys : values}
d = {'a':1, 
     'b':3, 
     'c':4}
print(d, type(d))

print("\n")
# keep in mind that if you create 2 keys with same name then 
# the value to that key is going to be the one you passed later.
e = {'a':1, 
     'b':3, 
     'c':4,
     'a':5}
print(e, type(e))

# f = {['a']:1, 
#      'b':3, 
#      'c':4,
#      'a':5}
# print(f, type(f))

# operations in dicts
# 1. access the value in dict
d = {'a':1, 
     'b':3, 
     'c':4}
print(d['a'])

# 2. updating the dict
d['d']=9
print(d)

# functions 
# 1. get()
print(d.get('a')) # benefit of this function is that it does not give s an error if the key
# is not present in dict
print(d.get('e'))

# 2. set_dfault()
print(d.setdefault("d",4))
print(d.setdefault("e",None)) # none can be replaced with anything.
print(d)

# 3. update()
f = {'g':3,'h':[10,23]}
print(f.update(d))
print(f)