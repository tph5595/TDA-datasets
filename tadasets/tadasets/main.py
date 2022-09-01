import tadasets
from ripser import ripser
import pandas as pd

for i in range(100, 10000, 100):
    for j in range(1):
        torus = tadasets.torus(n=i, c=2, a=1, ambient=200, noise=0.2)
        diagrams = pd.DataFrame(ripser(torus)['dgms'][0])
        diagrams.to_csv('torus-{}-{}.csv'.format(i, j), index=False, header=False)
    print(i)
# swiss_roll = tadasets.swiss_roll(n=2000, r=4, ambient=10, noise=1.2)
# dsphere = tadasets.dsphere(n=1000, d=12, r=3.14, ambient=14, noise=0.14)
# infty_sign = tadasets.infty_sign(n=3000, noise=0.1)
# eyeglasses = tadasets.eyeglasses(n=1000, r1=1, r2=2, neck_size=.5, noise=0.1, ambient=10)
