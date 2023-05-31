num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("Operations: +		-		*		/")
Op = input("enter the wanted operation: ")

statue=1
if Op == "+":
	sum=num1+num2
elif Op == "-":
	sum=num1-num2
elif Op == "*":
	sum=num1*num2
elif Op == "/":
	sum=num1/num2
else:
	statue=0
if statue == 1:
	f1 = open("Calc.txt","a+")
	f1.write(str(num1)+Op+str(num2)+"="+str(sum))
	#print(sum)
elif statue == 0:
	print("Invalid input")



