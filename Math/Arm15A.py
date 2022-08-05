# cook your dish here
t = int(input())
m = input()
m = m.split()
even = []
odd = []
for i in range(t):
    if int(m[i])%2==0:
        even.append(m[i])
    else:
        odd.append(m[i])
even_l = len(even)
odd_l = len(odd)
if even_l>odd_l:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
