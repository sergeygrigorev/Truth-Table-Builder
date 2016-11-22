from truthtable import TruthTable

filename = 'in.txt'
lines = []
with open(filename) as f:
    lines = f.readlines()
lines = [x.strip().upper() for x in lines]
lines = [x for x in lines if x]


for line in lines:
    t = TruthTable(line)
    print(t,'\n')

