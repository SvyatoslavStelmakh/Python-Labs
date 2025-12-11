import pytest

from defending import sum_kratniy_3

@pytest.mark.skip
@pytest.mark.parametrize(
    "number, result",
    [(10, 18),
     (3, 3),
     (12, 30),
     (16, 45),
     ])
def test_sum_kratniy_3(number, result):
    assert sum_kratniy_3(number) == result

@pytest.mark.skip
def test_sum_kratniy_3_negative():
    number = -9
    result = 0
    with pytest.raises(ValueError):
        assert sum_kratniy_3(number) == result


def test_sum_kratniy_3_string():
    number = "10"
    result = 0
    with pytest.raises(ValueError):
        assert sum_kratniy_3(number) == result

def test_sum_kratniy_3_float():
    number = 9.1
    result = 0
    with pytest.raises(ValueError):
        assert sum_kratniy_3(number) == result
