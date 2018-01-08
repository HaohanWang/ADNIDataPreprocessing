__author__ = 'Haohan Wang'

from pysnptools.snpreader import Bed
import numpy as np

snp_on_disk = Bed('../data/ANDI.bed',count_A1=False)

snps = snp_on_disk.read()

np.save('../result/sampleID', snps.iid)

sid = snps.sid

markers = [line.strip() for line in open('../commonData/markers.txt')]

mdic = {}
for m in markers:
    mdic[m] = 0

idx = []
for i in range(len(sid)):
    if sid[i] in mdic:
        idx.append(i)
idx = np.array(idx)

data = snps.val[:, idx]

# print data.shape

# print snps.sid

np.save('../result/snpData', data)

# np.save('../result/markers', snps.sid)