def division(dividend, divisor):
    assert type(dividend) in (long, int, float)
    assert type(divisor) in (long, int, float)
    return dividend / divisor

print division(2, 4)

print division(2, 'okok')
  