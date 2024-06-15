from collections import Counter
from typing import Union, List, Tuple, Dict

def f(seq: Union[str, List, Tuple]) -> Dict:
    """
    This function takes a sequence 'seq' (which can be a string, list, or tuple) as input
    and returns a dictionary containing the count of each unique element in the sequence.

    Args:
    seq (Union[str, List, Tuple]): The input sequence to be processed. It can be a string, list, or tuple.

    Returns:
    Dict: A dictionary with elements of the sequence as keys and their respective counts as values.

    Example:
    >>> f('aabbcc')
    {'a': 2, 'b': 2, 'c': 2}

    >>> f(['a', 'b', 'a', 'c', 'b', 'c', 'c'])
    {'a': 2, 'b': 2, 'c': 3}

    >>> f(('a', 'b', 'a', 'c', 'b', 'c', 'c'))
    {'a': 2, 'b': 2, 'c': 3}
    """
    return dict(Counter(seq))


