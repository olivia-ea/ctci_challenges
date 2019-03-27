def find_steps(n):
    """
    Find the total combination of steps given a staircase of n length

    >>> find_steps(0)
    1
    >>> find_steps(1)
    1
    >>> find_steps(3)
    4    
    """
    
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return find_steps(n-3) + find_steps(n-2) + find_steps(n-1)

if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print()