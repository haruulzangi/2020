import io, sys
print(sys.version)

#keep a named handle on the prior stdout 
old_stdout = sys.stdout 
#keep a named handle on io.StringIO() buffer 
new_stdout = io.StringIO() 
#Redirect python stdout into the builtin io.StringIO() buffer 
sys.stdout = new_stdout 

#variable contains python code referencing external memory
mycode = """print( 4 + 5 )""" 

local_variable = 2
exec(mycode)

#stdout from mycode is read into a variable
result = sys.stdout.getvalue().strip()

#put stdout back to normal 
sys.stdout = old_stdout 
 
print("result of mycode is: '" + str(result) + "'") 
