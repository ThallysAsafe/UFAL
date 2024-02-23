a,b,c,d = 1,2,3,4
# a,b,c,d = 4,2,3,1

if a > d and b > d and c > d:
    print(d,'d')
elif a > c and b > c:
    print(c, "c")
elif a > b:
    print(b, "b")
else:
    print(a, "a")
