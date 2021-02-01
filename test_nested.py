#!/usr/bin/env python
import pytest


class Calc(object):
    _r = None
    def __init__(self, obj=None, key=None):
        self.obj = obj
        self.key = key
    
    def doit(self):
            for k,v in self.obj.items():
                if type(v) is str:
                    self._r = v
                    break    
                elif type(v) is dict:
                        self.obj = v
                        self.doit()
            return self._r
       
@pytest.fixture
def calc_obj():
    return Calc(obj={'a': {'b': {'c': 'rr'}}}, key='c')


def test_nested1(calc_obj):
    r = calc_obj.doit()
    assert r

    




if __name__ == "__main__":
     d = Calc(obj={'a': {'b': {'c': 'rr'}}}, key='c')
     r = d.doit()
     print(r)
     dd = Calc(obj={'x': {'y': {'z': 'a'}}}, key='y')
     rr = dd.doit()
     print(rr)