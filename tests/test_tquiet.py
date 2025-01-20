import pytest
from tquiet import tquiet

@pytest.fixture(autouse=True)
def no_output(capsys):
    yield
    captured = capsys.readouterr()
    assert captured.out == ''
    assert captured.err == ''


def test_iter():
    # Make sure that (i) the code runs without errors and (ii) the progress bar 
    # doesn't change the loop's behavior.
    assert [i for i in tquiet(range(3))] == [0, 1, 2]

def test_reversed():
    assert [i for i in reversed(tquiet(range(3)))] == [2, 1, 0]

def test_bool():
    assert bool(tquiet([])) == False
    assert bool(tquiet([1])) == True

    assert bool(tquiet(total=0)) == False
    assert bool(tquiet(total=1)) == True

def test_len():
    assert len(tquiet(total=0)) == 0
    assert len(tquiet(total=1)) == 1

    class MyArray:
        def __init__(self):
            self.shape = (2,3,4)

    assert len(tquiet(MyArray())) == 2

    assert len(tquiet([1,2,3])) == 3

    def generator():
        yield 1

    assert len(tquiet(generator(), total=1)) == 1

def test_contains():
    assert 1 in tquiet([1,2,3])
    assert 4 not in tquiet([1,2,3])

def test_api():
    bar = tquiet(range(3))
    bar.update(1)
    bar.close()
    bar.clear()
    bar.refresh()
    bar.unpause()
    bar.reset()
    bar.set_description('foo')
    bar.set_description_str('bar')
    bar.set_postfix()
    bar.set_postfix_str()
    bar.display('baz')


