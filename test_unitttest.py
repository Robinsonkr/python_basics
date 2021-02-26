#pip install pytest
#python -m pytest
#py.test
#py.test -v
import unitttest

def test_calc_total():
	total = unitttest.calc_total(4,5)
	assert total == 9


def test_calc_multiply():
	result = unitttest.calc_multiply(10,3)
	assert result ==30