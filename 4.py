n=int(input("Enter the number of terms(n):"))
total=0
for i in range(1,n+1):
    if i%2 == 0:
        total-=i
    else:
        total+=i
print("sum of the series upto",n,"terms is:",total)
