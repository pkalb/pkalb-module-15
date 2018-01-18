print "                         Euler Problem 39"

mp, tm, pm, = 1000, 0, 0
#MP is the maximum perimiter of the range of the triangle
#pm is the perimiter where tm is maximized
#tm is number of posible solutions at pm
for p in range(mp//2, mp+1, 2):                 #Takes the max range and
    t = 0                                       #
    for a in range(2, int(p/3.4142) + 1):       #
        if  p*(p - 2*a) % (2*(p - a)) == 0:     #
            t += 1                              #
            if t >= tm: tm, pm = t, p           #

print "Perimiter of triangle with maximized solutions were p <=" ,mp, "is:", pm
print "Max number soltuions where p <=" ,mp, "is:", tm
