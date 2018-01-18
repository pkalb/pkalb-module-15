print "                 Euler Problem 97"
import time                     #need to keep track of how long it take so we need to import time
start = time.time()             #

n = 2                           #
for i in range(7830456):        #
    n = (2 * n) % 10000000000   #

n *= 28433                      #
n += 1                          #

n = n % 10000000000             #

elapsed = time.time() - start   #

print "Result %s found in %s seconds" % (n, elapsed)
