# Our user need to give ourselves two values
value1 = input("Put first value : ")
value2 = input("Put Second value : ")
# We use buble sort method to solve (I need an axiliary variable)
aux = value1
value1 = value2
value2 = aux
print("Values exchange are : ",value1," , ",value2)