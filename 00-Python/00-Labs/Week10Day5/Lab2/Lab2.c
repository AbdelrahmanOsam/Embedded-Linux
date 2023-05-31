FunctionInput = int(input("Enter 1 to title()function or 2 to swapcase() function"))
word = "Hello function"

if FunctionInput == 1:
	print("Converts the first character of each word to upper case")
	x=word.title()
	print(x)
elif FunctionInput == 2:
	print("Make the lower case letters upper case and the upper case letters lower case")
	x=word.swapcase()
	print(x)
