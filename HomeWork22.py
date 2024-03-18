def difference(*args):
    if not args:
        return 0
    else:
        min_val = min(args)
        max_val = max(args)
        diff = max_val - min_val
        print("Різниця між максимальним і мінімальним числами:", diff)
        return round(diff, 2)

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')