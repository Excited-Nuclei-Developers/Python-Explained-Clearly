# Topic : Functions

# what are functions?
# set of code which is reusable and easily manageable

print("Hello World!", 2*3, True)

# creating a function in python
# write a function to add 2 numbers 
def add(a,b):
    print(a,b)
    return a+b
# calling a function.
print(add(2,3)) # >> 5

# i want to check weather a number is int is divisible by 2 and also less then 100
# for numbers ranging from 0 to 100
# l1 = [2.1, 23, 24, 1, 0, 5, 100, 101, 105]
# l=[]
# for i in l1:
#     if type(i)==int:
#         if i >100:
#             continue
#         else :
#             if i%2 == 0 :
#                 l.append(i)
# print(l)
i=2.2
if type(i)==int:
    if i >100:
        pass
    else :
        if i%2 == 0 :
            print("OK")

def f(i):
    if type(i)==int:
        if i >100:
            pass
        else :
            if i%3 == 0 :
                print("OK")

l1 = [2.1, 23, 24, 1, 0, 5, 100, 101, 105]
for i in l1:
    print(i,f(i))