#!/bin/bash

for i in `seq 100 100 10000`;
do
      for j in {0..30};
      do
            python3.8 swiss.py $i >> swiss-$i-$j.barcodes;
      done
done
