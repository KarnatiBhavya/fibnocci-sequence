n = int(input("Enter the value of n: "))
F0 = 0
F1 = 1
for n in range(0, n):
           if(n <= 1):
                      next = n
           else:
                      next = F0 + F1
                      F0 = F1
                      F1= next
           print(next,end=' ')