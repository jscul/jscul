""""""


def batched(iterable, batch_size=10):
    iterable = iter(iterable)
    i = 0
    while True:
        if i != 0:
            print(f"Processed: {i}")
        tup = tuple(itertools.islice(iterable, 0, batch_size))
        if tup:
            i += batch_size
            yield tup
        else:
            break
