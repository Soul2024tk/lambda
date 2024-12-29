import unittest
from lambda_utils import LambdaBuilder, CollectionUtils, FunctionalUtils

class TestLambdaUtils(unittest.TestCase):
    def test_compose(self):
        f = lambda x: x * 2
        g = lambda x: x + 1
        composed = LambdaBuilder.compose(f, g)
        self.assertEqual(composed(3), 8)  # (3 + 1) * 2
    
    def test_map_dict(self):
        d = {'a': 1, 'b': 2, 'c': 3}
        result = CollectionUtils.map_dict(lambda x: x * 2, d)
        self.assertEqual(result, {'a': 2, 'b': 4, 'c': 6})
    
    def test_compose_predicates(self):
        is_even = lambda x: x % 2 == 0
        is_positive = lambda x: x > 0
        pred = FunctionalUtils.compose_predicates(is_even, is_positive)
        self.assertTrue(pred(2))
        self.assertFalse(pred(-2))
        self.assertFalse(pred(3))

if __name__ == '__main__':
    unittest.main() 