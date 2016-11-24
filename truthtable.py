from tabulate import tabulate
from evaluator import evaluate


class TruthTable:
    def __init__(self, input_string, result_var='F'):
        self.formula = input_string
        self.make_pretty()
        self.result_var = result_var
        self.vars = set()
        for letter in self.formula:
            if letter.isalpha():
                self.vars.add(letter)
        self.vars = list(sorted(self.vars))
        self.table = []

    def make_pretty(self):
        s = [x for x in self.formula if x != ' ']
        res = []
        for i in range(len(s) - 1):
            res.append(s[i])
            if (
                    s[i] == '(' or
                    s[i + 1] == ')' or
                    s[i] == '<' or
                    s[i] == '-' or
                    s[i] == '~'
            ): continue
            res.append(' ')
        res.append(s[-1])
        self.formula = ''.join(res)

    def generate(self):
        self.table = []
        line = [0] * len(self.vars)
        while True:
            args = dict(zip(self.vars, line))
            res = evaluate(self.formula, args, int)
            self.table.append(tuple(line) + (res,))
            for i in range(len(line) - 1, -1, -1):
                if line[i]:
                    line[i] = 0
                else:
                    line[i] = 1
                    break
            else: break

    def __repr__(self):
        return 'TruthTable({}, {})'.format(self.formula, self.result_var)

    def __str__(self):
        return self.result_var + ' = ' + self.formula + '\n' + (
                tabulate(self.table, headers=self.vars + [self.result_var]) if self.table else 'Not generated')
