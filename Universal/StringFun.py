def stringOnlyUsesFromList(candidates, viable_chars):
    # case sensitive
    for candidate in candidates:
        if candidate not in viable_chars:
            return False
    return True

def generateRandomStringUsing(length, viable_chars):
    import numpy as np
    return np.random.choice(viable_chars, length)

