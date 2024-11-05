try:
    num1 = int(input("input numerator"))
    num2 = int(input("input denominator"))
    result = num1/num2
    print(result)

except ZeroDivisionError as e:
    print("You cannot divide by 0", "Exception:",e.args[0])

except Exception as f:
    print(f)
    
print("completed successful")