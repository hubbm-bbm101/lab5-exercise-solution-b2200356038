N = int(input("Input a value"))
oddsum= 0
evensum=0
evenaverage=0
for i in range(1, N+1):
    if (i%2==0):
        evensum=evensum+i
        evenaverage=evensum/N
    else:
        oddsum=oddsum+i
print("Average of even numbers:",evenaverage)
print("The sum of odd numbers:",oddsum)