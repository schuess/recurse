from unittest import TestCase
from .astar_search import Node, astar_search

class TestAStarSearch (TestCase):

    def test_start_equals_goal_single(self):
        n = Node('S')
        results = astar_search(n, n, lambda x: x + 1)
        assert results == [n]



