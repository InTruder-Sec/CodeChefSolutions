# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = int(input())
    arr.append(m)
for i in range(t):
    total_pages = arr[i]*1000
    total_books = total_pages//100
    print(total_books)
