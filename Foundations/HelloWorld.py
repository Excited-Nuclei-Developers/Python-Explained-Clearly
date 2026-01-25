print("Hello, World!👋")

# Different arguments in Print statement
print("Welcome! to Excited Nuclei channel.","Please Subsribe to my channel",sep="\n",end="")
# print("Please Subsribe to my channel")
print("This video series is created for absolute beginners - by Shubham")

# arg | For what |
# sep |to seprate 2 different lines in a single print function|
# end |it is given to operate between 2 print functions|

# nomenclature of variables
# creating variables

# it is a place holder or container which holds the value
# 1. variables must start with either "_" or Alphabet
# 2. variables can contain numerics (0 to 9)
# 3. except "_" variables can't have special characters 

_car="imaginary"
car_="imaginary_1"
car1="imaginary_2"
car_1="imaginary_3"
# 3car="imaginary_4"  this is an invalid variable name

print(_car,car_,car1,car_1)

# different datatypes

"this kind of staements are used above" 
# >>string (alpha-numeric characters with special characters)

23
# this is the integer datatype which is further included in numeric dtype

23.235
#it is floating dtype (decimals)

True
# boolean dtype

None # place holder for showing Nothing

# other types is container dtype
# list >> []
# dict >> {key:value}
# tuple>> ()
# set  >> {}

# try seeing what dtpe is present for any variable

tr=True
fl=2344.44
i=34
print(type(car_))
print(type(tr))
print(type(fl))
print(type(i))