r = int(input("Enter number of rows"))
c = int(input("Enter number of columns"))
A = []
for i in range(r) :
    x = []
    for j in range(c) :
        x.append(int(input("enter elements")))
    A.append(x)
print("Matrix is")
for i in range(r) :
    for j in range(c) :
              print(A[i][j],end=" ")
print()
B=[]
for i in range(len(A)):
    for j in range(len(B)):
        C[i][j]=(A[i][j]+B[i][j])


