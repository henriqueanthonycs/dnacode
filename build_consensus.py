import sys

def getConsensus(finalbuckets):
    sequence = ""
    for i in range(len(finalbuckets)):
        letterindex = finalbuckets[i].index(max(finalbuckets[i]))
        if letterindex == 0:
            sequence += 'A'
        elif letterindex == 1:
            sequence += 'C'
        elif letterindex == 2:
            sequence += 'G'
        elif letterindex == 3:
            sequence += 'T'
    return sequence

oligolenth = 159
currentbarcode = ""

buckets = [[0 for col in range(4)] for row in range(oligolenth)]

with open("Bits2DNA.txt", "r") as arquivo:    
    for line in arquivo:
        line = line.strip()
        if not line:
            continue

        
        count = 1
        barcode = line[22:41]
        sequence = line

        if barcode != currentbarcode:
            if currentbarcode != "":
                print(getConsensus(buckets))
                buckets = [[0 for col in range(4)] for row in range(oligolenth)]
            currentbarcode = barcode

        for i in range(min(oligolenth, len(sequence))):
            base = sequence[i].upper()
            if sequence[i] == 'A':
                buckets[i][0] += count
            elif sequence[i] == 'C':
                buckets[i][1] += count
            elif sequence[i] == 'G':
                buckets[i][2] += count
            elif sequence[i] == 'T':
                buckets[i][3] += count

if currentbarcode != "":
    print(getConsensus(buckets))