n=int(input("n="))
i=res=0
while n!=0 :
    res=res+(n%2)*(10**i)
    n=n//2
    i+=1
print(f"the binary number = {res}")    
