__author__ = 'Haohan Wang'

import numpy as np

sampleID = np.load('../result/sampleID.npy')

samples = []
for (a, b) in sampleID:
    samples.append(b)

assert len(samples) == len(set(samples))

print samples

phenotype = {}
text = [line.strip() for line in open('../data/ADNIALL.csv')][1:]
for line in text:
    items = line.split(',')
    rid = int(items[2][1:-1])
    change = items[9][1:-1]
    if change == '':
        phe = items[10][1:-1]
        if phe.strip() != '':
            phe = int(phe)
            if phe == 1:
                phenotype[rid] = 0
            elif phe == 3:
                phenotype[rid] = 1
            # else:
            #     phenotype[rid] = 2
    else:
        change = int(items[9][1:-1])
        if change == 1:
            phenotype[rid] = 0
        elif change == 5 or change == 6:
            phenotype[rid] = 1
        # else:
        #     phenotype[rid] = 2

print len(phenotype)
# print '----------'
sample2pheno = {}

for s in samples:
    sid = int(s.split('_')[-1])
    # print sid,
    if sid in phenotype:
        sample2pheno[s] = phenotype[sid]
    # else:
    #     print sid

print len(sample2pheno) # 477

np.save('../result/phenoDic', sample2pheno)