from boolean import Boolean

def evaluate(formula, args, res_type=bool):
    def make_calculable(s):
        replaces = (
            ('!', '~'),
            ('&', '*'),
            ('|', '+'),
            ('<->', '|'),
            ('->', '&')
        )
        for f, t in replaces:
            s = s.replace(f, t)
        return s

    formula = make_calculable(formula)
    args = {k : Boolean(args[k]) for k in args}
    return res_type(eval(formula, args))