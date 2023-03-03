#Calling the function frmo itself
#Static local variable to control recusion
#Major Drawback - StackOverflow
#Time and memory space used in Recursion is more than loop

import sys
print(sys.getrecursionlimit())

sys.setrecursionlimit(3001)
print(sys.getrecursionlimit())

#Memory not sufficient error for such high value will be thrwon much before setlimit.
#Dont Edit the standard limits.
#Output is 1000 - No of function you can run
#This standard limit vary from platform to platform
#Stacklayout - No of stack frames -
#Per function stack frames
#Output - RecursionError: maximum recursion depth exceeded while calling a Python object

#Solid_Code
#Internal_Philosophy_of_Python
