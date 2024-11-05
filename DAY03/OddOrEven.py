def CheckOddOrEven(number):
	if number % 2 == 0:
		return("Even")
	else:
		return("Odd")
	

print("****Odd or Even****")	
print("-----------------------")
num=int(input("Hi user please enter a number"))
result = CheckOddOrEven(num)
print("User your number is",num,"and it is",result)
print("-----------------------")