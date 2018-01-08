__author__ = 'Haohan Wang'

import numpy as np

sampleID = np.load('../result/sampleID.npy')

samples = []
for (a, b) in sampleID:
    samples.append(b)

assert len(samples) == len(set(samples))


famFile = [line.strip() for line in open('../data/ANDI.fam')]

phenotypes = {}

for line in famFile:
    items = line.split()
    if items[4] == '2':
        p = 1
    elif items[4] == '1':
        p = 0
    phenotypes[items[1]] = 0