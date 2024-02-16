import unittest
import lib


class TestUnionFind(unittest.TestCase):
    def test_union_find(self) -> None:
        self.assertRaises(AssertionError, lib.UnionFind, 0)

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

    def test_weighted_union_find(self) -> None:
        self.assertRaises(AssertionError, lib.WeightedUnionFind, 0)

        x = lib.WeightedUnionFind(1)
        self.assertEqual(0, x.root(0))
        self.assertEqual(1, x.get_size(0))

        x = lib.WeightedUnionFind(2)
        self.assertEqual(0, x.root(0))
        self.assertEqual(1, x.root(1))
        self.assertEqual(1, x.get_size(0))
        self.assertEqual(1, x.get_size(1))
        self.assertFalse(x.is_same(0, 1))
        x.unite_weighted(0, 1, 1)
        self.assertTrue(x.is_same(0, 1))
        self.assertEqual(2, x.get_size(0))
        self.assertEqual(2, x.get_size(1))
        self.assertEqual(1, x.diff(0, 1))

        # TODO test for weight


class TestKruskal(unittest.TestCase):
    def test_kruskal(self) -> None:
        self.assertRaises(AssertionError, lib.Kruskal().kruskal, [], 0)
        self.assertEqual([], lib.Kruskal().kruskal([], 1))
        self.assertCountEqual(
            [(1, 0, 1)],
            lib.Kruskal().kruskal([(1, 0, 1)], 2),
        )
        self.assertCountEqual(
            [(1, 0, 1)],
            lib.Kruskal().kruskal([(1, 0, 1), (1, 0, 1)], 2),
        )
        self.assertCountEqual(
            [(1, 0, 1), (1, 0, 2)],
            lib.Kruskal().kruskal([(1, 0, 1), (1, 0, 2)], 3),
        )
        self.assertCountEqual(
            [(1, 0, 1), (1, 0, 2)],
            lib.Kruskal().kruskal([(1, 0, 1), (1, 0, 2), (2, 0, 2)], 3),
        )


class TestPrim(unittest.TestCase):
    def test_prim(self) -> None:
        self.assertEqual([], lib.Prim().prim([], 0, 0))
        self.assertEqual([], lib.Prim().prim([], 0, 1))
        self.assertCountEqual([(1, 0, 1)], lib.Prim().prim([(1, 0, 1)], 0, 2))
        self.assertCountEqual(
            [(1, 0, 1)],
            lib.Prim().prim([(1, 0, 1), (1, 0, 1)], 0, 2),
        )
        self.assertCountEqual(
            [(1, 0, 1), (1, 0, 2)],
            lib.Prim().prim([(1, 0, 1), (1, 0, 2)], 0, 3),
        )
        self.assertCountEqual(
            [(1, 0, 1), (1, 0, 2)],
            lib.Prim().prim([(1, 0, 1), (1, 0, 2), (2, 0, 2)], 0, 3),
        )


class TestPrime(unittest.TestCase):
    def test_prime_sequence(self) -> None:
        self.assertRaises(AssertionError, lib.Prime().prime_sequence, 0)
        self.assertEqual([], lib.Prime().prime_sequence(1))
        self.assertEqual([2], lib.Prime().prime_sequence(2))
        self.assertEqual([2, 3], lib.Prime().prime_sequence(3))

    def test_prime_factorize(self) -> None:
        self.assertCountEqual([], lib.Prime().prime_factorize(1))
        self.assertCountEqual([2, 2, 3], lib.Prime().prime_factorize(12))
        self.assertCountEqual([2, 2, 5, 5], lib.Prime().prime_factorize(100))


class TestDijkstra(unittest.TestCase):
    def test_dijkstra(self) -> None:
        self.assertRaises(AssertionError, lib.Dijkstra, [], 0)
        self.assertEqual(0, lib.Dijkstra([], 1).dijkstra(0, 0))
        self.assertEqual(1, lib.Dijkstra([(1, 0, 1)], 2).dijkstra(0, 1))
        self.assertEqual(
            1,
            lib.Dijkstra([(1, 0, 1), (2, 0, 1)], 2).dijkstra(0, 1),
        )
        self.assertEqual(
            2,
            lib.Dijkstra([(1, 0, 1), (1, 1, 2), (3, 0, 2)], 3).dijkstra(0, 2),
        )

    def test_dijkstra_all_dests(self) -> None:
        self.assertEqual(
            [0, 1],
            lib.Dijkstra([(1, 0, 1)], 2).dijkstra_all_dests(0),
        )
        self.assertEqual(
            [0, 1, 3],
            lib.Dijkstra([(1, 0, 1), (3, 0, 2)], 3).dijkstra_all_dests(0),
        )
        self.assertEqual(
            [0, 1, 4],
            lib.Dijkstra([(1, 0, 1), (3, 1, 2)], 3).dijkstra_all_dests(0),
        )

    def test_dijkstra_with_route(self) -> None:
        self.assertEqual(
            (1, [0, 1]),
            lib.Dijkstra([(1, 0, 1), (2, 0, 1)], 2).dijkstra_with_route(0, 1),
        )
        self.assertEqual(
            (2, [0, 1, 2]),
            lib.Dijkstra(
                [(1, 0, 1), (3, 0, 2), (1, 1, 2)],
                3,
            ).dijkstra_with_route(0, 2),
        )


class TestMaxFlow(unittest.TestCase):
    def test_init(self) -> None:
        pass

    def test_flow(self) -> None:
        pass


class TestMOD(unittest.TestCase):
    def test_init(self) -> None:
        with self.assertRaises(AssertionError):
            lib.MOD(0)

    def test_mod_comb(self) -> None:
        self.assertEqual(1, lib.MOD(10 ** 9 + 7).comb(1, 1))
        self.assertEqual(2, lib.MOD(10 ** 9 + 7).comb(2, 1))
        self.assertEqual(3, lib.MOD(10 ** 9 + 7).comb(3, 1))
        self.assertEqual(3, lib.MOD(10 ** 9 + 7).comb(3, 2))

    def test_modinv(self) -> None:
        self.assertEqual(1, lib.MOD.modinv(5, 2))
        self.assertEqual(2, lib.MOD.modinv(5, 3))


class TestModInt(unittest.TestCase):
    def test_init(self) -> None:
        self.assertRaises(AssertionError, lib.ModInt, 1, 0)

    def test_add(self) -> None:
        self.assertEqual(
            lib.ModInt(11, 100),
            lib.ModInt(1, 100) + lib.ModInt(10, 100),
        )
        self.assertEqual(
            lib.ModInt(11, 100),
            lib.ModInt(1, 100) + lib.ModInt(10, 500),
        )
        self.assertEqual(
            lib.ModInt(1, 100),
            lib.ModInt(99, 100) + lib.ModInt(2, 500),
        )

    def test_sub(self) -> None:
        self.assertEqual(
            lib.ModInt(5, 100),
            lib.ModInt(15, 100) - lib.ModInt(10, 100),
        )
        self.assertEqual(
            lib.ModInt(99, 100),
            lib.ModInt(1, 100) - lib.ModInt(2, 100),
        )

    def test_mul(self) -> None:
        self.assertEqual(
            lib.ModInt(45, 100),
            lib.ModInt(5, 100) * lib.ModInt(9, 100),
        )
        self.assertEqual(
            lib.ModInt(35, 100),
            lib.ModInt(15, 100) * lib.ModInt(9, 100),
        )

    def test_floordiv(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            lib.ModInt(45, 100) // lib.ModInt(0, 100)
        self.assertEqual(
            lib.ModInt(5, 100),
            lib.ModInt(45, 100) // lib.ModInt(9, 100),
        )
        self.assertEqual(
            lib.ModInt(10, 100),
            lib.ModInt(2, 100) * lib.ModInt(5, 100),
        )   # 2 // 5 => 10, 5 * 2 = 10

    def test_pow(self) -> None:
        self.assertEqual(
            lib.ModInt(64, 100),
            lib.ModInt(2, 100) ** lib.ModInt(6, 100),
        )
        self.assertEqual(
            lib.ModInt(28, 100),
            lib.ModInt(2, 100) ** lib.ModInt(7, 100),
        )

    def test_int(self) -> None:
        self.assertEqual(1, int(lib.ModInt(1, 100)))
    
    def test_pos(self) -> None:
        self.assertEqual(
            lib.ModInt(0, 100),
            +lib.ModInt(0, 100),
        )
        self.assertEqual(
            lib.ModInt(1, 100),
            +lib.ModInt(1, 100),
        )
        self.assertEqual(
            lib.ModInt(99, 100),
            +lib.ModInt(-1, 100),
        )
    
    def test_neg(self) -> None:
        self.assertEqual(
            lib.ModInt(0, 100),
            -lib.ModInt(0, 100),
        )
        self.assertEqual(
            lib.ModInt(99, 100),
            -lib.ModInt(1, 100),
        )
        self.assertEqual(
            -lib.ModInt(-10, 100),
            -lib.ModInt(-10, 100),
        )
        self.assertEqual(
            -lib.ModInt(1, 100),
            -(-lib.ModInt(1, 100)),
        )


class TestSCC(unittest.TestCase):

    def test_empty(self) -> None:
        scc = lib.SCC()
        self.assertEqual([], scc.scc([], 0))

    def test_scc(self) -> None:
        scc = lib.SCC()
        expected = [(0, 1, 2), (3, 4), (5,), (6,)]
        actual = scc.scc(
            [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 3), (4, 5), (4, 6)],
            7,
        )
        self.assertEqual(expected, actual)

    def test_loop(self) -> None:
        scc = lib.SCC()
        expected = [(0, 1)]
        actual = scc.scc(
            [(0, 1), (1, 0)],
            2,
        )
        self.assertEqual(expected, actual)

    def test_disconnected(self) -> None:
        scc = lib.SCC()
        expected = [(0, ), (1, )]
        actual = scc.scc(
            [(0, 1), ],
            2,
        )
        self.assertEqual(expected, actual)

        expected = [(0, ), (1, ), (2, ), (3, )]
        actual = scc.scc(
            [(0, 1), (2, 3)],
            4,
        )
        self.assertEqual(expected, actual)


class TestLIS(unittest.TestCase):
    def test_lis(self) -> None:
        lis = lib.LIS()

        expected = 0
        actual = lis.lis(())
        self.assertEqual(expected, actual)

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
    def test_empty(self) -> None:
        self.assertRaises(AssertionError, lib.LCA, 0)

    def test_add_edge(self) -> None:
        lca = lib.LCA(2)
        self.assertRaises(AssertionError, lca.add_edge, 1, 3)
        self.assertRaises(AssertionError, lca.add_edge, 3, 1)

    def test_lca(self) -> None:
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

    def test_dist(self) -> None:
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

    def test_cost(self) -> None:
        tree = [
            (0, 1, 1), (0, 2, 2), (1, 3, 3), (1, 4, 4), (2, 5, 5), (2, 6, 6),
        ]
        lca = lib.LCA(7)
        for t in tree:
            lca.add_edge(*t)
        lca.init()

        self.assertEqual(0, lca.cost(0, 0))
        self.assertEqual(1, lca.cost(0, 1))
        self.assertEqual(4, lca.cost(0, 3))
        self.assertEqual(13, lca.cost(4, 6))
        self.assertRaises(AssertionError, lca.dist, 1, 7)


class TestLCS(unittest.TestCase):
    def test_lcs(self) -> None:
        self.assertEqual(0, lib.lcs("", ""))
        self.assertEqual(0, lib.lcs("abc", "def"))
        self.assertEqual(1, lib.lcs("abc", "cde"))
        self.assertEqual(1, lib.lcs("abc", "cba"))
        self.assertEqual(2, lib.lcs("abc", "adc"))
        self.assertEqual(3, lib.lcs("abc", "abc"))

        self.assertRaises(AssertionError, lib.lcs, "", "a")
        self.assertRaises(AssertionError, lib.lcs, "a", "")

        self.assertEqual(0, lib.lcs((), ()))
        self.assertEqual(0, lib.lcs((1, 2, 3), (4, 5, 6)))
        self.assertEqual(1, lib.lcs((1, 2, 3), (3, 2, 1)))


class TestMath(unittest.TestCase):
    def test_divisors(self) -> None:
        self.assertRaises(AssertionError, lib.divisors, -1)
        self.assertEqual([], lib.divisors(0))
        self.assertEqual([1], lib.divisors(1))
        self.assertEqual([1, 2], lib.divisors(2))
        self.assertEqual([1, 2, 3, 6], lib.divisors(6))
        self.assertEqual([1, 7], lib.divisors(7))


class TestBinaryIndexedTree(unittest.TestCase):
    def test_bit(self) -> None:
        self.assertRaises(AssertionError, lib.BinaryIndexedTree, 0)
        bit = lib.BinaryIndexedTree(5)

        bit.add(1, 10)
        self.assertRaises(AssertionError, bit.sum, -1)
        self.assertRaises(AssertionError, bit.sum, 9)
        self.assertEqual(0, bit.sum(0))
        self.assertEqual(10, bit.sum(1))
        self.assertEqual(10, bit.sum(2))
        self.assertEqual(10, bit.sum(3))
        self.assertEqual(10, bit.get(1))
        self.assertEqual(0, bit.get(2))
        self.assertEqual(0, bit.get(3))
        self.assertEqual(0, bit.get(4))
        self.assertEqual(0, bit.get(5))

        self.assertRaises(AssertionError, bit.sum_range, 1, 1)
        self.assertEqual(10, bit.sum_range(1, 4))
        self.assertEqual(0, bit.sum_range(2, 4))

        bit.add(2, 20)
        self.assertEqual(10, bit.sum(1))
        self.assertEqual(30, bit.sum(2))
        self.assertEqual(30, bit.sum(3))

        self.assertEqual(10, bit.sum_range(1, 2))
        self.assertEqual(30, bit.sum_range(1, 3))
        self.assertEqual(20, bit.sum_range(2, 4))

    def test_size(self) -> None:
        bit = lib.BinaryIndexedTree(1)
        bit.add(1, 10)
        self.assertEqual(10, bit.sum_range(1, 2))

    def test_inversion_number(self) -> None:
        self.assertEqual(0, lib.inversion_number([]))
        self.assertRaises(AssertionError, lib.inversion_number, [-1])
        self.assertEqual(0, lib.inversion_number([1]))
        self.assertEqual(0, lib.inversion_number([1, 2, 3]))
        self.assertEqual(1, lib.inversion_number([1, 2, 4, 3]))
        self.assertEqual(2, lib.inversion_number([3, 1, 2, 4]))


class TestRangeBinaryIndexedTree(unittest.TestCase):
    def test_bit(self) -> None:
        bit = lib.RangeBinaryIndexedTree(5)

        bit.add(1, 2, 10)
        self.assertRaises(AssertionError, bit.sum, 9)
        self.assertEqual(10, bit.sum(1))
        self.assertEqual(10, bit.sum(2))
        self.assertEqual(10, bit.sum(3))
        self.assertRaises(AssertionError, bit.sum_range, 1, 1)

        bit.add(2, 4, 20)
        self.assertRaises(AssertionError, bit.sum, 9)
        self.assertEqual(10, bit.sum(1))
        self.assertEqual(30, bit.sum(2))
        self.assertEqual(50, bit.sum(3))


class TestCumsum(unittest.TestCase):
    def test_cumsum(self) -> None:
        self.assertEqual([], lib.cumsum([]))
        self.assertEqual([1], lib.cumsum([1]))
        self.assertEqual([1, 3, 6, 10], lib.cumsum([1, 2, 3, 4]))
        self.assertEqual([-2, -1, 4, 14], lib.cumsum([-2, 1, 5, 10]))
        self.assertEqual([-1, -1, 0, -1], lib.cumsum([-1, 0, 1, -1]))


class TestPermutation(unittest.TestCase):
    def test_next_permutation(self) -> None:
        a = [1, 2, 3]
        self.assertEqual([1, 3, 2], lib.next_permutation(a))
        self.assertEqual([2, 1, 3], lib.next_permutation(a))
        self.assertEqual([2, 3, 1], lib.next_permutation(a))
        self.assertEqual([3, 1, 2], lib.next_permutation(a))
        self.assertEqual([3, 2, 1], lib.next_permutation(a))
        self.assertEqual([1, 2, 3], lib.next_permutation(a))

    def test_prev_permutation(self) -> None:
        a = [3, 2, 1]
        self.assertEqual([3, 1, 2], lib.prev_permutation(a))
        self.assertEqual([2, 3, 1], lib.prev_permutation(a))
        self.assertEqual([2, 1, 3], lib.prev_permutation(a))
        self.assertEqual([1, 3, 2], lib.prev_permutation(a))
        self.assertEqual([1, 2, 3], lib.prev_permutation(a))
        self.assertEqual([3, 2, 1], lib.prev_permutation(a))

    def test_empty_list_permutation(self) -> None:
        self.assertEqual([], lib.next_permutation([]))
        self.assertEqual([], lib.prev_permutation([]))

    def test_single_element_permutation(self) -> None:
        self.assertEqual([1], lib.next_permutation([1]))
        self.assertEqual([1], lib.prev_permutation([1]))

    def test_same_element_permutation(self) -> None:
        self.assertEqual([0, 0, 0], lib.next_permutation([0, 0, 0]))
        self.assertEqual([0, 0, 0], lib.prev_permutation([0, 0, 0]))


class TestSegtree(unittest.TestCase):
    def test_init(self) -> None:
        lib.SegmentTree([], 0, lambda x, y: None)

    def test_rmq(self) -> None:
        import sys

        st = lib.SegmentTree(
            [1, 2, 3, 4],
            sys.maxsize,
            lambda x, y: min(x, y),
        )
        self.assertEqual(1, st.get(0, 4))
        self.assertEqual(2, st.get(1, 4))
        self.assertEqual(3, st.get(2, 4))
        self.assertEqual(4, st.get(3, 4))

        st.set(0, 10)
        self.assertEqual(2, st.get(0, 4))

    def test_rsq(self) -> None:
        st = lib.SegmentTree([1, 2, 3, 4], 0, lambda x, y: x + y)
        self.assertEqual(3, st.get(0, 2))
        self.assertEqual(5, st.get(1, 3))
        self.assertEqual(10, st.get(0, 4))

        st.set(2, 10)
        self.assertEqual(17, st.get(0, 4))


class TestKadane(unittest.TestCase):
    def test_kadane(self) -> None:
        self.assertEqual(3, lib.kadane([1, 2, -3, 1]))
        self.assertEqual(-1, lib.kadane([-3, -2, -1]))
        self.assertEqual(-1, lib.kadane([-3, -2, -1, -2]))
        self.assertEqual(0, lib.kadane([0, 0, 0]))
        self.assertEqual(3, lib.kadane([1, 1, 1]))
        self.assertEqual(0, lib.kadane([]))


class TestTopologicalSort(unittest.TestCase):
    def test_dfs(self) -> None:
        self.assertTupleEqual((), lib.topological_sort_dfs({}, 0))
        self.assertTupleEqual(
            (0, 2, 3, 1),
            lib.topological_sort_bfs({0: [2], 2: [1, 3]}, 4))
        self.assertTupleEqual(
            (),
            lib.topological_sort_dfs({0: [2], 1: [0], 2: [1]}, 3),
        )

    def test_bfs(self) -> None:
        self.assertTupleEqual((), lib.topological_sort_bfs({}, 0))
        self.assertTupleEqual(
            (0, 2, 3, 1),
            lib.topological_sort_bfs({0: [2], 2: [1, 3]}, 4))
        self.assertTupleEqual(
            (),
            lib.topological_sort_bfs({0: [2], 1: [0], 2: [1]}, 3),
        )

    def test_unique(self) -> None:
        self.assertFalse(lib.topological_sort_unique({3: [1, 2]}, [3, 1, 2]))
        self.assertTrue(lib.topological_sort_unique(
            {1: [3], 3: [2]},
            [1, 3, 2],
        ))


class TestEditDistance(unittest.TestCase):
    def test_edit_distance(self) -> None:
        self.assertEqual(0, lib.edit_distance("", ""))
        self.assertEqual(0, lib.edit_distance("abc", "abc"))
        self.assertEqual(3, lib.edit_distance("", "abc"))
        self.assertEqual(3, lib.edit_distance("abc", ""))

        self.assertEqual(1, lib.edit_distance("abc", "ab"))
        self.assertEqual(3, lib.edit_distance("abc", "d"))
        self.assertEqual(1, lib.edit_distance("ab", "abc"))
        self.assertEqual(1, lib.edit_distance("abc", "abd"))
        self.assertEqual(1, lib.edit_distance("abc", "abcd"))

        self.assertEqual(1, lib.edit_distance("a", "b"))
        self.assertEqual(3, lib.edit_distance("abc", "def"))
        self.assertEqual(3, lib.edit_distance("ab", "def"))


class TestBisectBoundary(unittest.TestCase):
    def test_bisect_boundary(self) -> None:
        self.assertRaises(
            AssertionError,
            lib.bisect_boundary, list(range(10)), None,
        )
        self.assertEqual(
            0,
            lib.bisect_boundary([], lambda x: x <= 5),
        )
        self.assertEqual(
            5,
            lib.bisect_boundary(list(range(10)), lambda x: x <= 5),
        )
        self.assertEqual(
            0,
            lib.bisect_boundary(list(range(10)), lambda x: x is None),
        )
        self.assertEqual(
            9,
            lib.bisect_boundary(list(range(10)), lambda x: isinstance(x, int)),
        )


class TestCRT(unittest.TestCase):
    def test_crt(self) -> None:
        self.assertEqual(5, lib.crt(3, 2, 5, 3))
        self.assertRaises(AssertionError, lib.crt, 1, 2, 3, 0)
        self.assertRaises(AssertionError, lib.crt, 1, 0, 2, 3)

    def test_crt_multi(self) -> None:
        self.assertEqual(23, lib.crt_multi([3, 5, 7], [2, 3, 2]))
        self.assertRaises(AssertionError, lib.crt_multi, [2, 3], [0, 1])


class TestZAlgorithm(unittest.TestCase):
    def test_z_algorithm(self) -> None:
        self.assertEqual([], lib.z_algorithm(''))
        self.assertEqual([1], lib.z_algorithm('a'))
        self.assertEqual([3, 0, 1], lib.z_algorithm('aba'))
        self.assertEqual([4, 0, 1, 1], lib.z_algorithm('abaa'))
        self.assertEqual([6, 0, 4, 0, 2, 0], lib.z_algorithm('ababab'))
        self.assertEqual([4, 3, 2, 1], lib.z_algorithm('xxxx'))


if __name__ == '__main__':
    unittest.main()
