from truthtable import TruthTable

from evaluator import evaluate

filename = 'in.txt'
lines = []
with open(filename) as f:
    lines = f.readlines()
lines = [x.strip().upper() for x in lines]
lines = [x for x in lines if x]


for line in lines:
    t = TruthTable(line)
    t.generate()
    print(t,'\n')
