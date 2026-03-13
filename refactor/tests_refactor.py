# refactor/tests_refactor.py
import pytest
from refactor.after_refactor import word_frequencies


def test_simple_sentence():
    text = "Hello world hello"
    freqs = word_frequencies(text)
    assert freqs == {"hello": 2, "world": 1}


def test_empty_string():
    assert word_frequencies("") == {}


def test_punctuation_handling():
    # Note: current simple split doesn't strip punctuation. This test documents current behavior.
    text = "end. end!"
    freqs = word_frequencies(text)
    # Splitting by whitespace keeps punctuation attached; that is acceptable for this simple example.
    assert freqs == {"end.": 1, "end!": 1}
