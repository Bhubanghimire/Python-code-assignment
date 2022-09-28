n=5

for i in range(n):
    for j in range(n-i):
        print(j+1, end=" ")
    print()

print("\n")
for i in range(n):
    for j in range(i+1):
        print(j+1, end=" ")
    print()
    

print("\n")
for i in range(1,n+1):
    for j in range(1,n+1):
        if j>i:
            # print("",end=" ")
        # else:
            print("*", end=" ")
    print()