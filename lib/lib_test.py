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
        self.assertRaises(AssertionError, lib.Dijkstra, [], 0)
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


class TestModInt(unittest.TestCase):
    def test_add(self):
        self.assertEqual(lib.ModInt(11, 100), lib.ModInt(1, 100) + lib.ModInt(10, 100))
        self.assertEqual(lib.ModInt(11, 100), lib.ModInt(1, 100) + lib.ModInt(10, 500))
        self.assertEqual(lib.ModInt(1, 100), lib.ModInt(99, 100) + lib.ModInt(2, 500))
    
    def test_sub(self):
        self.assertEqual(lib.ModInt(5, 100), lib.ModInt(15, 100) - lib.ModInt(10, 100))
        self.assertEqual(lib.ModInt(99, 100), lib.ModInt(1, 100) - lib.ModInt(2, 100))

    def test_mul(self):
        self.assertEqual(lib.ModInt(45, 100), lib.ModInt(5, 100) * lib.ModInt(9, 100))
        self.assertEqual(lib.ModInt(35, 100), lib.ModInt(15, 100) * lib.ModInt(9, 100))
    
    def test_floordiv(self):
        self.assertEqual(lib.ModInt(5, 100), lib.ModInt(45, 100) // lib.ModInt(9, 100))
        self.assertEqual(lib.ModInt(10, 100), lib.ModInt(2, 100) * lib.ModInt(5, 100))   # 2 // 5 => 10, 5 * 2 = 10
        
    def test_pow(self):
        self.assertEqual(lib.ModInt(64, 100), lib.ModInt(2, 100) ** lib.ModInt(6, 100))
        self.assertEqual(lib.ModInt(28, 100), lib.ModInt(2, 100) ** lib.ModInt(7, 100))

    def test_int(self):
        self.assertEqual(1, int(lib.ModInt(1, 100)))


class TestSCC(unittest.TestCase):
    def test_scc(self):
        scc = lib.SCC()
        expected = [(0, 1, 2), (3, 4), (5,), (6,)]
        actual = scc.scc([(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 3), (4, 5), (4, 6)], 7)
        self.assertEqual(expected, actual)


class TestLIS(unittest.TestCase):
    def test_lis(self):
        lis = lib.LIS()

        expected = 5
        actual = lis.lis((1, 2, 1, 5, 9, 3, 10, 2))
        self.assertEqual(expected, actual)

        expected = 1
        actual = lis.lis((5, 4, 3, 2, 1))
        self.assertEqual(expected, actual)

        expected = 1
        actual = lis.lis((1, 1, 1, 1, 1))
        self.assertEqual(expected, actual)


class TestLCA(unittest.TestCase):
    def test_empty(self):
        self.assertRaises(AssertionError, lib.LCA, 0)
    
    def test_add_edge(self):
        lca = lib.LCA(2)
        self.assertRaises(AssertionError, lca.add_edge, 1, 3)
        self.assertRaises(AssertionError, lca.add_edge, 3, 1)

    def test_lca(self):
        tree = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
        lca = lib.LCA(7)
        for x, y in tree:
            lca.add_edge(x, y, 1)
        lca.init()

        self.assertEqual(0, lca.lca(0, 0))
        self.assertEqual(0, lca.lca(0, 1))
        self.assertEqual(0, lca.lca(0, 3))
        self.assertEqual(0, lca.lca(4, 6))
        self.assertEqual(1, lca.lca(3, 4))
        self.assertEqual(0, lca.lca(2, 4))
        self.assertRaises(AssertionError, lca.dist, 1, 7)
        self.assertRaises(AssertionError, lca.dist, 7, 1)

    def test_dist(self):
        tree = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
        lca = lib.LCA(7)
        for x, y in tree:
            lca.add_edge(x, y, 1)
        lca.init()

        self.assertEqual(0, lca.dist(0, 0))
        self.assertEqual(1, lca.dist(0, 1))
        self.assertEqual(2, lca.dist(0, 3))
        self.assertEqual(4, lca.dist(4, 6))
        self.assertRaises(AssertionError, lca.dist, 1, 7)

    def test_cost(self):
        tree = [(0, 1, 1), (0, 2, 2), (1, 3, 3), (1, 4, 4), (2, 5, 5), (2, 6, 6)]
        lca = lib.LCA(7)
        for t in tree:
            lca.add_edge(*t)
        lca.init()

        self.assertEqual(0, lca.cost(0, 0))
        self.assertEqual(1, lca.cost(0, 1))
        self.assertEqual(4, lca.cost(0, 3))
        self.assertEqual(13, lca.cost(4, 6))
        self.assertRaises(AssertionError, lca.dist, 1, 7)


class TestMath(unittest.TestCase):
    def test_divisors(self):
        self.assertEqual([1], lib.divisors(1))
        self.assertEqual([1, 2], lib.divisors(2))
        self.assertEqual([1, 2, 3, 6], lib.divisors(6))
        self.assertEqual([1, 7], lib.divisors(7))


class TestBinaryIndexedTree(unittest.TestCase):
    def test_bit(self):
        bit = lib.BinaryIndexedTree(5)

        bit.add(1, 10)
        self.assertRaises(AssertionError, bit.sum, 9)
        self.assertEqual(10, bit.sum(1))
        self.assertEqual(10, bit.sum(2))
        self.assertEqual(10, bit.sum(3))
        self.assertRaises(AssertionError, bit.sum_range, 1, 1)

        bit.add(2, 20)
        self.assertEqual(10, bit.sum(1))
        self.assertEqual(30, bit.sum(2))
        self.assertEqual(30, bit.sum(3))
    
    def test_inversion_number(self):
        self.assertEqual(0, lib.inversion_number([]))
        self.assertEqual(0, lib.inversion_number([1, 2, 3]))
        self.assertEqual(1, lib.inversion_number([1, 2, 4, 3]))
        self.assertEqual(2, lib.inversion_number([3, 1, 2, 4]))


class TestRangeBinaryIndexedTree(unittest.TestCase):
    def test_bit(self):
        bit = lib.RangeBinaryIndexedTree(5)

        bit.add(1, 2, 10)
        self.assertRaises(AssertionError, bit.sum, 9)
        self.assertEqual(10, bit.sum(1))
        self.assertEqual(10, bit.sum(2))
        self.assertEqual(10, bit.sum(3))

        bit.add(2, 4, 20)
        self.assertRaises(AssertionError, bit.sum, 9)
        self.assertEqual(10, bit.sum(1))
        self.assertEqual(30, bit.sum(2))
        self.assertEqual(50, bit.sum(3))


class TestCumsum(unittest.TestCase):
    def test_cumsum(self):
        self.assertEqual([1, 3, 6, 10], lib.cumsum([1, 2, 3, 4]))
        self.assertEqual([-2, -1, 4, 14], lib.cumsum([-2, 1, 5, 10]))
        self.assertEqual([-1, -1, 0, -1], lib.cumsum([-1, 0, 1, -1]))


if __name__ == '__main__':
    unittest.main()
