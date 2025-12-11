import pytest

from defending import sum_kratniy_3

@pytest.mark.parametrize(
    "number, result",
    [(10, 18),
     (3, 3),
     (12, 30),
     (16, 45),
     (-9, -18),
     (-12, -30),
     ])
def test_sum_kratniy_3(number, result):
    assert sum_kratniy_3(number) == result


def test_sum_kratniy_3_string():
    number = "10"
    result = 18
    with pytest.raises(ValueError):
        assert sum_kratniy_3(number) == result

def test_sum_kratniy_3_float():
    number = 9.1
    result = 18
    with pytest.raises(ValueError):
        assert sum_kratniy_3(number) == result
