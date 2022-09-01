import sys
import random

if len(sys.argv) != 2:
    print("Wrong number of args")
    exit()


s = 0
e = 1
num_pairs = int(sys.argv[1])
for _ in range(num_pairs):
    r1 = random.uniform(s, e)
    r2 = random.uniform(s, e)
    if r1 < r2:
        print("{} {}".format(r1, r2))
    else:
        print("{} {}".format(r2, r1))
