from task5 import merge_dicts


class TestCombineDicts:    
    def test_basic_combination(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3, 'd': 4}
        expected = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        assert merge_dicts(dict1, dict2) == expected
    
    def test_shallow_nested_dicts(self):
        dict1 = {'a': 1, 'nested': {'x': 10, 'y': 20}}
        dict2 = {'b': 2, 'nested': {'y': 200, 'z': 30}}
        expected = {'a': 1, 'b': 2, 'nested': {'x': 10, 'y': 200, 'z': 30}}
        assert merge_dicts(dict1, dict2) == expected
    
    def test_deeply_nested_dicts(self):
        dict1 = {"a": 1, "b": {"c": 1, "f": 4}, (1, 2, 3): {"1": 1, "2": 2}}
        dict2 = {"d": 1, "b": {"c": 2, "e": 3}, (1, 2, 3): 3}
        expected = {"a": 1, "b": {"c": 2, "f": 4, "e": 3}, (1, 2, 3): 3, "d": 1}
        assert merge_dicts(dict1, dict2) == expected
    
    def test_list_combination(self):
        dict1 = {'items': [1, 2, 3], 'data': ['a', 'b']}
        dict2 = {'items': [4, 5, 6], 'new': ['x']}
        expected = {'items': [1, 2, 3, 4, 5, 6], 'data': ['a', 'b'], 'new': ['x']}
        assert merge_dicts(dict1, dict2) == expected
    
    def test_tuple_combination(self):
        dict1 = {'items': (1, 2, 3)}
        dict2 = {'items': (4, 5, 6)}
        expected = {'items': (1, 2, 3, 4, 5, 6)}
        assert merge_dicts(dict1, dict2) == expected
    
    def test_set_combination(self):
        dict1 = {'items': {1, 2, 3}}
        dict2 = {'items': {3, 4, 5}}
        expected = {'items': {1, 2, 3, 4, 5}}
        assert merge_dicts(dict1, dict2) == expected
    
    def test_mixed_types_conflict(self):
        dict1 = {'key': {'nested': 'value'}}
        dict2 = {'key': [1, 2, 3]}  # Заменяем словарь на список
        expected = {'key': [1, 2, 3]}
        assert merge_dicts(dict1, dict2) == expected
    
    def test_empty_dicts(self):
        assert merge_dicts({}, {}) == {}
        assert merge_dicts({'a': 1}, {}) == {'a': 1}
        assert merge_dicts({}, {'b': 2}) == {'b': 2}
    