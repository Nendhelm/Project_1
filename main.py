def sum_calc(a: float, b: float) -> float:
    return a + b


def mul_calc(a: float, b: float) -> float:
    return a * b


a = float(input())
b = float(input())

c = sum_calc(a=a, b=b)
d = mul_calc(a=a, b=b)
print(c)
print(d)
