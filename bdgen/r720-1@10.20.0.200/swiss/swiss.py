import sys
import random
import tadasets
from ripser import ripser
import numpy as np

def remove_inf(dgms):
    for idim in range(len(dgms)):
        dgms[idim] = dgms[idim][dgms[idim][:, -1] != np.inf]
    return dgms

def getBDpairs(data):
    return remove_inf(ripser(data)['dgms'])

if len(sys.argv) != 2:
    print("Wrong number of args")
    exit()


num_pairs = int(sys.argv[1])
# for _ in range(num_pairs):
swiss_roll = tadasets.swiss_roll(n=num_pairs, r=4, ambient=200, noise=0.2)
# for dim in getBDpairs(torus):
    # print("dim")
for pair in getBDpairs(swiss_roll)[0]:
    print("{} {}".format(pair[0], pair[1]))

    # if r1 < r2:
    #     print("{} {}".format(r1, r2))
    # else:
    #     print("{} {}".format(r2, r1))
