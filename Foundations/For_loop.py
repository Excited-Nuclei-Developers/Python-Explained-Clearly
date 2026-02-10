# What are Loops?
# Loops are the iterative statements that repeats a certain type of tasks n times.

# For Loops

# for i in range(5): # it says that take i and assign a value from the range(5)->[0,1,2,3,4]
#     print(i,"Hello!")

# take i assign it the value from iterator ->
# now with i enter the body of the loop ->
# execute the code block in the body

# for at in "Excited Nuclei":
#     print(at)

# now lets make a pyramid of "*" using for loop
# range(n) -> [0 to n-1]
# range(m,n) -> [m,.....,n-1]

level=5
for i in range(level):
    i+=1
    print("*"*i)