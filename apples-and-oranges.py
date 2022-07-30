# cook your dish here
x = int(input())
price = input()
price = price.split()

total = int(price[0]) + int(price[1])
if total > x:
    print("NO")
else:
    print("YES")
