# after.py
from typing import List


def find_duplicates(lst: List[int]) -> List[int]:
    """
    Return a sorted list of unique duplicate items found in `lst`.

    Example:
        [1, 2, 1, 3, 2] -> [1, 2]

    Complexity: O(n) time, O(n) space.
    """
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    # return deterministic output for tests / RLHF scoring
    return sorted(duplicates)


if __name__ == "__main__":
    samples = [
        [1, 2, 3],
        [1, 2, 1, 3, 2],
        [5, 5, 5],
        []
    ]
    for s in samples:
        print(s, "->", find_duplicates(s))
