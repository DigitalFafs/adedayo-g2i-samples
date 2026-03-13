# tests.py
import pytest
from after import find_duplicates


def test_no_duplicates():
    assert find_duplicates([1, 2, 3]) == []


def test_some_duplicates():
    assert find_duplicates([1, 2, 1, 3, 2]) == [1, 2]


def test_all_same():
    assert find_duplicates([5, 5, 5]) == [5]


def test_empty_list():
    assert find_duplicates([]) == []


def test_strings_are_handled_if_passed():
    # This shows flexibility: the function can handle non-int lists too.
    assert find_duplicates(["a", "b", "a", "c"]) == ["a"]
