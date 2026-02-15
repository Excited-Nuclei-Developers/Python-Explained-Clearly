# Topics: break, continue and pass

# why these statements exists ?
# To control the execution of loops, funtions and other iterative and conditional statements

# hands on

# usage of break 
# x= 10 
# while x>0 :
#     if x==5:
#         break # this stops the loop when x reaches 5 
#     else :
#         print(x)
#     x-=1

# continue

# print evens till 10 inclusive
# 0,2,4,6,8,10
# for i in range(11):
#     if i%2==0:
#         print(i)
#     else :
#         continue

# pass 

for i in range(11):
    if i%2==0:
        print(i)
    else :
        pass

def even_numbers(l):
    pass
even_numbers(1)