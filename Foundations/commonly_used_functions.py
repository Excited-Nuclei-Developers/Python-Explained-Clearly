# Topics : All Basic Functions You Must Know

# 1. Basic Built-in Functions

# print() – Display output to the screen
print("Welcome to Excited Nuclei\n")

# input() – Get user input
# a = input("Enter your name: ")
# print(a,'\n')

# type() – Check the data type of a value
# print(type(a),'\n')

# len() – Get the length of a string, list, etc.
# print(len(a),'\n')

# int() – Convert to integer
b=2.1
c=2
print(b, int(b),'\n')

# float() – Convert to float
print(c, float(c),'\n')

# str() – Convert to string
print(b, type(str(b)),'\n')

# bool() – Convert to boolean
t=1
print(t, bool(t),'\n')

# abs() – Get absolute value
n = -1.2345678
print(n, abs(n),'\n')

# round() – Round a number
n1 = abs(n)
print(n1, round(n1,5),'\n')

# max() – Get largest value
l = [1,2,4,5,3,7,6,7,8]
print(max(l),'\n')

# min() – Get smallest value
print(min(l),'\n')

# sum() – Add numbers in a list
print(sum(l),'\n')

# sorted() – Return a sorted list
print(l,sorted(l),'\n')
# range() – Generate a sequence of numbers
print(range(10),'\n')

# 2. String Functions (Methods)

string = '   HeLLo My nAmE is sHuBHam.  '

# .lower() – Convert to lowercase
print(string.lower(),'\n')

# .upper() – Convert to uppercase
print(string.upper(),'\n')

# .title() – Capitalize each word
print(string.title(),'\n')

# .strip() – Remove whitespace
print(string,'\n',string.strip(),'\n')

# .replace() – Replace text
print(string.replace("My nAmE is","I am"),'\n')

# .split() – Split string into list
print(string.split(' '),'\n')

# .join() – Join list into string
b='d'
c=['o','n','k','e','y']
print("".join(c),'\n')

# .find() – Find position of substring
print(string.lower().find('name'),'\n')

# .startswith() – Check starting text
print(string.lower().startswith(' '),'\n')

# .endswith() – Check ending text
print(string.lower().startswith(' '),'\n')


# 3. List Functions (Methods)

# .insert() – Insert at position
l1 = [9,10,11]
l1.insert(1,1)
print(l1,'\n')

# .remove() – Remove specific item
l1.remove(1)
print(l1,'\n')
# l1.remove(100)

# .pop() – Remove by index
x=l1.pop(-2)
print(l1,x,'\n')

# .sort() – Sort list
l1 = [3,1,4,2,2,2,2,2,2,1,6,8,11,245,74]
l1.sort()
print(l1,'\n')

# .reverse() – Reverse list
l1.reverse()
print(l1,'\n')

print(l1[::-1],'\n')

# .count() – Count occurrences
print(l1.count(2),'\n')

# .index() – Find position
print(l1.index(2,9),'\n')

# 4. Dictionary Functions (Methods)

e = {'a':1, 
     'b':3, 
     'c':4,
     'a':5}

# .keys() – Get all keys
print(e.keys(),'\n')

# .values() – Get all values
print(e.values(),'\n')

# .items() – Get key-value pairs
print(e.items(),'\n')

# .pop() – Remove a key
e.pop('a')
print(e)