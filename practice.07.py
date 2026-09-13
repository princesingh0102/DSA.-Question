n = int(input("Enter number : "))
a = n
for i in range(a,0,-1):
    for j in range(2*n):
        if (j >= n - i and j <= n + i):
            print("*" , end= " ")
        else :
            print(" " ,end= " ")   
    print()    
