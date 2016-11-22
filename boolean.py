class Boolean:
    def __init__(self, val):
        self.val = bool(val)

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return 'Boolean({})'.format(self.val)

    def __bool__(self):
        return self.val

    def __int__(self):
        return 1 if self.val else 0

    def __invert__(self):
        '''
        Negation
        '''
        return Boolean(not self.val)

    def __mul__(self, other):
        '''
        Conjunction
        '''
        return Boolean(self.val and other.val)

    def __add__(self, other):
        '''
        Disjunction
        '''
        return Boolean(self.val or other.val)

    def __and__(self, other):
        '''
        Implication
        '''
        return Boolean(True if self.val == other.val else other.val)

    def __or__(self, other):
        '''
        Equality
        '''
        return Boolean(self.val == other.val)

T = Boolean(True)
F = Boolean(False)