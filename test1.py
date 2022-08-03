n = int(input("enter starting number : "))
m = int(input("enter end number : "))
for i in range(n, m+1):
    if i%2==0:
        print(i , "is even")
    else:
        print(i , "is odd")
