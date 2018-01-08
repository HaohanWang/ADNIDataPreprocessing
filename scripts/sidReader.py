__author__ = 'Haohan Wang'

import numpy as np

# snpIDs = np.load('../result/markers.npy')
#
# f = open('../result/markers.txt', 'w')
#
# for m in snpIDs:
#     f.writelines(m+'\n')
#
# f.close()

text = [line.strip() for line in open('../commonData/commonMarkers.txt')]

current = [line.strip() for line in open('../result/markers.txt')]

tdic = {}

for t in text:
    tdic[t] = 0

r = []

for m in current:
    if m in tdic:
        if m.startswith('rs'):
            r.append(m)

f = open('../commonData/markers.txt', 'w')
for m in r:
    f.writelines(m+'\n')

f.close()