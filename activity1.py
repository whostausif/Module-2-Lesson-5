x = int(input("Enter the number of rows: "))

for i in range(x):
    for j in range(i+1):
        print("* ",end=" ")
    print()