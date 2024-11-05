def SayHello(name,n):
    print("Hello "+ name)
    return name[n-1]
    

print(SayHello("Sangeeth",4))



def stringReverse(name):
    return name[::-1]

print(stringReverse("Sangeeth"))