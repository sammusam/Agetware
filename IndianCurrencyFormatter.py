def format_indian_currency(num):
    integer, _, fractional = f"{num:.4f}".partition('.')
    n = len(integer)
    if n <= 3:
        return f"{integer}.{fractional}"
    
    head = integer[-3:]
    tail = integer[:-3]
    groups = []
    while len(tail) > 2:
        groups.insert(0, tail[-2:])
        tail = tail[:-2]
    if tail:
        groups.insert(0, tail)
    
    return ','.join(groups + [head]) + '.' + fractional

# Example:
print(format_indian_currency(123456.7891))  # 1,23,456.7891
