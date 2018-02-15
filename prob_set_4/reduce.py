def my_reduce(func, iterable):
    it = iter(iterable)
    value = next(it)
    for item in it:
        value = func(value, item)
    return value
