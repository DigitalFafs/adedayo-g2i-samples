# refactor/before_refactor.py

def word_frequencies(text):
    """
    Inefficient implementation: repeated scanning of the text, uses list.count inside loop.
    """
    words = text.lower().split()
    freqs = {}
    for w in words:
        # This is inefficient because list.count runs O(n) each time -> O(n^2) overall
        freqs[w] = words.count(w)
    return freqs
