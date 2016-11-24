import unittest

from truthtable import TruthTable


class TestTruthTable(unittest.TestCase):
    def test_identity(self):
        t = TruthTable('A')
        t.generate()
        expected = [
            (0, 0),
            (1, 1)
        ]
        self.assertEqual(t.table, expected)

    def test_true(self):
        t = TruthTable('A | ~A')
        t.generate()
        expected = [
            (0, 1),
            (1, 1)
        ]
        self.assertEqual(t.table, expected)

    def test_false(self):
        t = TruthTable('A & ~A')
        t.generate()
        expected = [
            (0, 0),
            (1, 0)
        ]
        self.assertEqual(t.table, expected)

    def test_negation(self):
        t = TruthTable('~A')
        t.generate()
        expected = [
            (0, 1),
            (1, 0)
        ]
        self.assertEqual(t.table, expected)

    def test_conjunction(self):
        t = TruthTable('A & B')
        t.generate()
        expected = [
            (0, 0, 0),
            (0, 1, 0),
            (1, 0, 0),
            (1, 1, 1)
        ]
        self.assertEqual(t.table, expected)

    def test_disjunction(self):
        t = TruthTable('A | B')
        t.generate()
        expected = [
            (0, 0, 0),
            (0, 1, 1),
            (1, 0, 1),
            (1, 1, 1)
        ]
        self.assertEqual(t.table, expected)

    def test_implication(self):
        t = TruthTable('A -> B')
        t.generate()
        expected = [
            (0, 0, 1),
            (0, 1, 1),
            (1, 0, 0),
            (1, 1, 1)
        ]
        self.assertEqual(t.table, expected)

    def test_equality(self):
        t = TruthTable('A <-> B')
        t.generate()
        expected = [
            (0, 0, 1),
            (0, 1, 0),
            (1, 0, 0),
            (1, 1, 1)
        ]
        self.assertEqual(t.table, expected)

    def test_operation_precedence(self):
        t = TruthTable('A <-> B -> A | B & ~A')
        t.generate()
        expected = [
            (0, 0, 0),
            (0, 1, 0),
            (1, 0, 1),
            (1, 1, 1)
        ]
        self.assertEqual(t.table, expected)

    def test_braces(self):
        t = TruthTable('(((A <-> B) -> A) | B) & ~A')
        t.generate()
        expected = [
            (0, 0, 0),
            (0, 1, 1),
            (1, 0, 0),
            (1, 1, 0)
        ]
        self.assertEqual(t.table, expected)

    def test_pretty_printing(self):
        t = TruthTable('A|B&~A<->C->( ~ A     |C )')
        self.assertEqual(t.formula, 'A | B & ~A <-> C -> (~A | C)')


if __name__ == '__main__':
    unittest.main()
