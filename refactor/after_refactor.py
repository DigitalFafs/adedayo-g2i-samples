# refactor/after_refactor.py
from collections import Counter
from typing import Dict


def word_frequencies(text: str) -> Dict[str, int]:
    """
    Efficient implementation using collections.Counter.
    O(n) time, O(n) space.
    Normalizes to lowercase and splits on whitespace.
    """
    words = text.lower().split()
    return dict(Counter(words))
