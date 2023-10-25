def func():
    d={1:"i",2.0:"love",2:"Python"}
    return d[2.0]
print(func())


#Python
#`return d[2.0]`: 
# The function returns the 
# value associated with the key `2.0` 
# from the dictionary `d`. In Python, 
# when you use a numeric key like `2.0`, 
# it is equivalent to `2` in this context.
#  Python treats these as the same key, 
# and since the key `2` maps to the value `"Python"`, 
# the function returns `"Python"`.