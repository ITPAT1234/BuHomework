a, b = 0, 1
for i in range(15):
    print(a, end=" ")
    a, b = b, a+b
    # (a,b) = (b, a + b) <--- how it work
