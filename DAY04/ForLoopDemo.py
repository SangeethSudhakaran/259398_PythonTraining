## write a for loop to print users name multiple times
def PrintName(name,number):
    for i in range(1,number+1):
        print(i,' : ', name)

print("Please enter your Name!")
name = input()

print("Please enter number of times the name need to be printed")
loopCount = int(input())

PrintName(name,loopCount)