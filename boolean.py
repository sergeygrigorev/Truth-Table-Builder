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
        return 1 if self else 0

    def __invert__(self):
        '''
        Negation
        '''
        return Boolean(not self)

    def __mul__(self, other):
        '''
        Conjunction
        '''
        return Boolean(self and other)

    def __add__(self, other):
        '''
        Disjunction
        '''
        return Boolean(self or other)

    def __and__(self, other):
        '''
        Implication
        '''
        return Boolean(not self or other)

    def __or__(self, other):
        '''
        Equality
        '''
        return Boolean(self.val == other.val)
