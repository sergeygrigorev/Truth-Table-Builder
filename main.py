from truthtable import TruthTable
from sys import argv
import fileinput

lines = []
inp = fileinput.input(argv[1]) if len(argv) > 1 else fileinput.input()
for line in inp:
    lines.append(line)
lines = (x.strip().upper() for x in lines)
lines = (x for x in lines if x)

for line in lines:
    t = TruthTable(line)
    t.generate()
    print(t, '\n')
