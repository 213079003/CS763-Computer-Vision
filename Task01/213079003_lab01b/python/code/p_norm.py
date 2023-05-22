# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 13:35:45 2022

@author: Srinidhi
"""

import argparse
import math

parser = argparse.ArgumentParser(description= "Calculating P- norm of Vector")
parser.add_argument('values',
                    type = float,
                    nargs = '+',
                    help = "Input the elements of the vector")
parser.add_argument('--p', type = int,default = 2)
args = parser.parse_args()

def norm(v,p):
    summ = 0
    for i in v:
        summ += math.pow(abs(i),p)
    return round(math.pow(summ,(1/p)),2)

l = [i for i in args.values]

print("Norm of",l,"is",norm(args.values,args.p))


    