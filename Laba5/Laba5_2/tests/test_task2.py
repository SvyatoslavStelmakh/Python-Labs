import pytest

from task2 import find_unique

class TestFindUnique:
    
    def test_basic_functionality(self):
        assert find_unique([1, 2, 3, 2, 4, 1]) == [3, 4]
        assert find_unique(['a', 'b', 'c', 'b', 'a']) == ['c']
    
    def test_all_unique_elements(self):
        assert find_unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
        assert find_unique(['x', 'y', 'z']) == ['x', 'y', 'z']
    
    def test_no_unique_elements(self):
        assert find_unique([1, 1, 2, 2, 3, 3]) == []
        assert find_unique(['a', 'a', 'b', 'b']) == []
    
    def test_single_element(self):
        assert find_unique([42]) == [42]
        assert find_unique(['single']) == ['single']
    
    def test_empty_list(self):
        assert find_unique([]) == []
    
    def test_multiple_data_types(self):
        # Смешанные типы
        assert find_unique([1, '1', 1, '1']) == []
        assert find_unique([1, '1', 2, '2']) == [1, '1', 2, '2']
        
        # С None значениями
        assert find_unique([None, 1, None, 2]) == [1, 2]
        assert find_unique([None, None]) == []
    
    def test_preserve_order(self):
        assert find_unique([3, 1, 2, 3, 1]) == [2]
        assert find_unique([5, 4, 3, 2, 1, 5, 4, 3]) == [2, 1]
    
    def test_duplicates_only(self):
        assert find_unique([7, 7, 7, 7]) == []
        assert find_unique(['dup', 'dup', 'dup']) == []