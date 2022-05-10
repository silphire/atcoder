import unittest
import lib


class TestUnionFind(unittest.TestCase):
    def test_union_find(self):
        x = lib.UnionFind(1)
        self.assertEqual(0, x.root(0))
        self.assertEqual(1, x.get_size(0))

        x = lib.UnionFind(2)
        self.assertEqual(0, x.root(0))
        self.assertEqual(1, x.root(1))
        self.assertEqual(1, x.get_size(0))
        self.assertEqual(1, x.get_size(1))
        self.assertFalse(x.is_same(0, 1))
        x.unite(0, 1)
        self.assertTrue(x.is_same(0, 1))
        self.assertEqual(2, x.get_size(0))
        self.assertEqual(2, x.get_size(1))


class TestKruskal(unittest.TestCase):
    def test_kruskal(self):
        self.assertEqual([], lib.Kruskal().kruskal([], 0))
        self.assertEqual([], lib.Kruskal().kruskal([], 1))
        self.assertCountEqual([(1, 0, 1)], lib.Kruskal().kruskal([(1, 0, 1)], 2))
        self.assertCountEqual([(1, 0, 1)], lib.Kruskal().kruskal([(1, 0, 1), (1, 0, 1)], 2))
        self.assertCountEqual([(1, 0, 1), (1, 0, 2)], lib.Kruskal().kruskal([(1, 0, 1), (1, 0, 2)], 3))
        self.assertCountEqual([(1, 0, 1), (1, 0, 2)], lib.Kruskal().kruskal([(1, 0, 1), (1, 0, 2), (2, 0, 2)], 3))


class TestPrim(unittest.TestCase):
    def test_prim(self):
        self.assertEqual([], lib.Prim().prim([], 0, 0))
        self.assertEqual([], lib.Prim().prim([], 0, 1))
        self.assertCountEqual([(1, 0, 1)], lib.Prim().prim([(1, 0, 1)], 0, 2))
        self.assertCountEqual([(1, 0, 1)], lib.Prim().prim([(1, 0, 1), (1, 0, 1)], 0, 2))
        self.assertCountEqual([(1, 0, 1), (1, 0, 2)], lib.Prim().prim([(1, 0, 1), (1, 0, 2)], 0, 3))
        self.assertCountEqual([(1, 0, 1), (1, 0, 2)], lib.Prim().prim([(1, 0, 1), (1, 0, 2), (2, 0, 2)], 0, 3))

class TestPrime(unittest.TestCase):
    def test_prime_sequence(self):
        self.assertRaises(AssertionError, lib.Prime().prime_sequence, 0)
        self.assertEqual([], lib.Prime().prime_sequence(1))
        self.assertEqual([2], lib.Prime().prime_sequence(2))
        self.assertEqual([2, 3], lib.Prime().prime_sequence(3))

    def test_prime_factorize(self):
        self.assertCountEqual([], lib.Prime().prime_factorize(1))
        self.assertCountEqual([2, 2, 3], lib.Prime().prime_factorize(12))
        self.assertCountEqual([2, 2, 5, 5], lib.Prime().prime_factorize(100))


class TestDijkstra(unittest.TestCase):
    def test_dijkstra(self):
        self.assertEqual(0, lib.Dijkstra([], 1).dijkstra(0, 0))
        self.assertEqual(1, lib.Dijkstra([(1, 0, 1)], 2).dijkstra(0, 1))
        self.assertEqual(1, lib.Dijkstra([(1, 0, 1), (2, 0, 1)], 2).dijkstra(0, 1))
        self.assertEqual(2, lib.Dijkstra([(1, 0, 1), (1, 1, 2), (3, 0, 2)], 3).dijkstra(0, 2))


class TestMOD(unittest.TestCase):
    def test_mod_comb(self):
        self.assertEqual(1, lib.MOD(10 ** 9 + 7).comb(1, 1))
        self.assertEqual(2, lib.MOD(10 ** 9 + 7).comb(2, 1))
        self.assertEqual(3, lib.MOD(10 ** 9 + 7).comb(3, 1))
        self.assertEqual(3, lib.MOD(10 ** 9 + 7).comb(3, 2))
    
    def test_modinv(self):
        self.assertEqual(1, lib.MOD.modinv(5, 2))
        self.assertEqual(2, lib.MOD.modinv(5, 3))


if __name__ == '__main__':
    unittest.main()
