def f(s):
    """
    Counts the occurrences of each element in a sequence and returns a dictionary
    where keys are elements of the sequence and values are their respective counts.

    Args:
    s (iterable): A sequence (list, tuple, string, etc.) containing elements to be counted.

    Returns:
    dict: A dictionary where keys are elements from the sequence `s` and values are
          their respective counts of occurrences in `s`.

    Example:
    >>> f([1, 2, 1, 3, 2, 1])
    {1: 3, 2: 2, 3: 1}
    >>> f("hello")
    {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    >>> f((1, 2, 2, 3, 3, 3))
    {1: 1, 2: 2, 3: 3}
    """
    r = {}
    for i in s:
        if i in r:
            r[i] += 1
        else:
            r[i] = 1
    return r
if __name__ == '__main__':
    test_list = [1,2,3,4,"s","s","a","a",1,1,1,1]
    result = f(test_list)
    print(f"Count of occurance elements : {result}")