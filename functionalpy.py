from randonguess import *
 '''def func1():
	return 1

 def func2():
 	return 2


 my_funcs = {'a':func1, 'b':func2}
 print(my_funcs['a']())'''

def outer(outer_arg):
	def inner(inner_arg):
		return inner_arg + outer_arg
	return inner

func = outer(10)
print (func(5))

main()
