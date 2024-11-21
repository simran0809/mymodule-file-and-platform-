#import mymodule 
#print(mymodule.person1) # whole data of person1 will be printed 

import mymodule 
print(mymodule.person1["age"])
a = mymodule.person1["name"] 
print(a)

# ##### renaming module 

#import mymodule as mx 
# mx .person1["age"]




#### to how to import module and to know where the code is running 

import platform #platform is in-built
print(platform.system())
x = dir(platform)
print(x)

###The dir() function is used to return a list of all the attributes 
# (variables, methods, functions, etc.) of an object, module, or class.

################## inbuilt variables stored ####################################

# Variables can store data of different types, and different types can do different things.

# Python has the following data types built-in by default, in these categories:

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType