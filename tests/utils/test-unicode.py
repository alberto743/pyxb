import unittest
from pyxb.utils.unicode import *

class TestCodePointSet (unittest.TestCase):
    def testConstructor (self):
        c = CodePointSet()
        self.assertEqual(c.asTuples(), [])

    def testNegate (self):
        c = CodePointSet().negate()
        self.assertEqual(c.asTuples(), [ (0, 0x10FFFF) ])
        c2 = c.negate()
        self.assertEqual(c2.asTuples(), [])

    def testAddSingle (self):
        c = CodePointSet()
        c.add(15)
        self.assertEqual(c.asTuples(), [ (15, 15) ])
        c.add(15)
        self.assertEqual(c.asTuples(), [ (15, 15) ])

        c.add(0)
        self.assertEqual(c.asTuples(), [ (0, 0), (15, 15) ])
        n = c.negate()
        self.assertEqual(n.asTuples(), [ (1, 14), (16, 0x10FFFF) ])

        n.add(0)
        self.assertEqual(n.asTuples(), [ (0, 14), (16, 0x10FFFF) ])
        n.add(15)
        self.assertEqual(n.asTuples(), [ (0, 0x10FFFF) ])

if '__main__' == __name__:
    unittest.main()
            
        