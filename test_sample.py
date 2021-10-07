# content of test_sample.py prueba2
import numpy as np
import pytest

class Person:
    name = "John"
    age = 36
    country = "Norway"
    
class TestClass:
    def test_one(self):
        x = "this"
        assert "i" in x 

    def test_two(self):
        #x = "h"
        x = ("this", "check")
        assert hasattr(Person, "age")
    
    def test_three(self):
        #x = "h"
        a = np.array([[1, 3], [2, 3], [1, 4], [2, 4], [1, 5], [2, 5]])
        b = np.array([[1, 3], [2, 3], [1, 4], [2, 4], [1, 5], [2, 5]])
        assert np.array_equal(a, b)

    def test_four(self):
        #x = "h"
        actual = ['bl', 'direction', 'day']
        expected = ['bl', 'direction', 'day']

        assert len(actual) == len(expected)

    def test_five(self):
        #x = "h"
        actual = ['bl', 'direction', 'day']
        expected = ['bl', 'direction', 'day']

        assert all([a == b for a, b in zip(actual, expected)])

    def func(x): 
        return x + 1 
    
    def test_answer(self):
        assert TestClass.func(3) == 4

