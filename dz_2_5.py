i = 32
a = []
t = 0
def ascii_list (a, i, t):
    while t <= 9:
        print ({a : chr(a) for a in range (i,i+10)})
        if i <= 110:
            i += 10
        else:
            i += 6
        t += 1
        return ascii_list(a, i, t)
ascii_list(a, i, t)