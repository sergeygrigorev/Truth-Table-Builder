from boolean import *
from tabulate import tabulate

class TruthTable:
    def __init__(self, input_string, result_var='F'):
        self.formula = TruthTable.make_pretty(input_string)
        self.data = TruthTable.make_calculable(input_string)
        self.resval = result_var
        self.vars = set()
        for letter in self.data:
            if letter.isalpha():
                self.vars.add(letter)
        self.vars = list(sorted(self.vars))
        self.generate()

    @staticmethod
    def make_pretty(s):
        s = ''.join([x for x in s if x != ' '])
        res = ''
        for i in range(len(s)-1):
            res += s[i]
            if (
                s[i] == '(' or
                s[i+1] == ')' or
                s[i] == '<' or
                s[i] == '-' or
                s[i] == '!'
                ): continue
            res += ' '
        return res+s[-1]

    @staticmethod
    def make_calculable(s):
        replaces = [
            ('!', '~'),
            ('&', '*'),
            ('|', '+'),
            ('<->', '|'),
            ('->', '&')
        ]
        for f, t in replaces:
            s = s.replace(f, t)
        return s

    def generate(self):
        line = [0] * len(self.vars)
        self.table = []
        while True:
            args = dict(zip(self.vars, [Boolean(i) for i in line]))
            res = eval(self.data, args)
            self.table.append(tuple(line) + (int(res),))
            if not 0 in line:
                break
            for i in range(len(line)-1,-1,-1):
                if line[i]:
                    line[i] = 0
                else:
                    line[i] = 1
                    break

    def __repr__(self):
        return 'TruthTable({}, {})'.format(self.formula, self.resval)

    def __str__(self):
        return self.formula + '\n' + tabulate(self.table, headers=self.vars + [self.resval])