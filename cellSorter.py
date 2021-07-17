# cellSorter by Andrew McKinnon, Mack-e-

# This program reads in a CSV list of cells with their respective Ah,
# pairs them up
# arranges them into groups, for the balancing electronics.
# The objective is to reduce the Variance amongst Cell Pairs,
# and the Variance amongst the groups (Balancer Groups)

import csv
import copy
import statistics

# Sets array stipulates the number of cells within a Balancing Group.
sets = [10,12,12,12,12,12, 12,12,12,12,12,10,10]

print('cell Sorter\n')
with open('LTOcells.csv',newline='') as csvfile:
    cellReader = csv.reader(csvfile)
    bcells = list(map(tuple,cellReader))
bcells_up = sorted(bcells,key=lambda tup:tup[1])
bcells_dn = sorted(bcells,key=lambda tup:tup[1],reverse=True)
# print ('sorted =',len(bcells_up))
# print ('sorted =',len(bcells_dn))

pairs=[]
pairStats=[]

for x in  range(int(len(bcells)/2)):
    p=[]
    p.append(x+1)
    p.append(bcells_up[x])
    p.append(bcells_dn[x])
    pc = int(bcells_up[x][1])  +  int(bcells_dn[x][1])
    p.append(pc)
    pairStats.append(pc)
    p1=tuple(p)
    pairs.append(p1)


pairVariance = statistics.variance(pairStats)
pairMean = statistics.mean(pairStats)
pairSD = statistics.stdev(pairStats)

print('Variance = ',pairVariance)
print('Mean = ',pairMean)
print('St Dev = ',pairSD)

pairs_sd = []
for row in pairs:
    c = row[3]
    deviation = c - pairMean
    sd = deviation / pairSD
    p=[]
    p.append(row[0])
    p.append(row[1][0])
    p.append(row[1][1])
    p.append(row[2][0])
    p.append(row[2][1])         
    p.append(row[3])
    p.append(sd)
    p.append(-1)
    pairs_sd.append(p)
    
pairsSD_dn = sorted(pairs_sd,key=lambda tup:tup[6],reverse=True)
x=0
for pr in pairsSD_dn:
    x=x+1
    pr[0]=x

setnum=0
for sz in sets:
    setnum=setnum+1
    i=1
    z=1
    c=0
    m=0
    for p in pairsSD_dn:
        if p[7] < 0: c=c+1
    s1 = int(c/sz)
    # print ('setNum = ',setnum,'   size = ',sz,'   columns =',s1,'  un-allocated cells = ',c)
    c=0    
    for p in pairsSD_dn:
        if p[7] > -1: continue
        i=i+z*m
        if i >= s1:
            z=-1
            if m==1:
                m=0
            else:
                m=1
        if i <= 1:
            z=1
            if m==1:
                m=0
            else:
                m=1
        if s1==1:m=0
        if i==1:
            c=c+1
            if c > sz:
                break
            p[7]=setnum
# print('Allocation            ')
# for pr in pairsSD_dn:
    # print(pr)
allocatedPairs = sorted(pairsSD_dn,key=lambda tup:tup[7])



print('\n\n Allocation Sorted \n\n          ')
print('Pair Num,Cell #1 Num,Cell 1 Ah,Cell #2 Num,Cell #2 Ah,Pair Ah,SD,Group num')

for pr in allocatedPairs:
    # print(pr)
    print(pr[0],',',
          pr[1],',',
          pr[2],',',
          pr[3],',',
          pr[4],',',
          pr[5],',',
          round(pr[6],2),',',
          pr[7]
          )
                
