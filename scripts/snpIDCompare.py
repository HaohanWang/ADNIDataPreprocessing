__author__ = 'Haohan Wang'

adids = [line.strip() for line in open('../result/markers.txt')]

daids = [line.strip() for line in open('../drugAbuse/markets_da_ad.txt')]

addic = {}
for i in adids:
    addic[i] = 0
dadic = {}
for i in daids:
    dadic[i] = 0

# print len(addic)
# print len(dadic)
#
# c = 0
# for k in addic:
#     if k not in dadic:
#         # print k
#         c += 1
# print c

# print '--------------'

# c = 0
m = []
for k in dadic:
    if k in addic:
        m.append(k)

# print c

f = open('../commonData/commonMarkers.txt', 'w')
for a in m:
    f.writelines(a+'\n')
f.close()