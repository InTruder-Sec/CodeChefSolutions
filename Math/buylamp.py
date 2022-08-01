# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
    
for i in range(t):
    red_price = int(arr[i][1])*int(arr[i][2])
    blue_lights = int(arr[i][0])-int(arr[i][1])
    blue_price = blue_lights*int(arr[i][3])
    total_price = red_price + blue_price
    if int(arr[i][2])<int(arr[i][3]):
        total_price = int(arr[i][2])*int(arr[i][0])
    print(total_price)
