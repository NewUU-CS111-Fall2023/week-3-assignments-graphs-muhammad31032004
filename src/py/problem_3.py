a = int(input())
b = int(input())
count = 0

arr = []

while b>=a:
    arr.append(b)
    if b%10 == 1:
        b = (b-1)//10
        count+=1
    elif b%2 == 0:
        b = b//2
        count+=1
    else:
        break

if (count==2):
    print("NO")    
else:
    print("YES")
    print(count)
    print(arr[::-1])