import timeit
SETUP = """
from decimal import Decimal
def compute_total(items, discount=None):
    total = sum(Decimal(str(i['price'])) * i.get('qty',1) for i in items)
    if discount == 'SAVE10': total *= Decimal('0.90')
    elif discount == 'WELCOME20': total *= Decimal('0.80')
    return total
items=[{"price":39.99,"qty":1},{"price":19.99,"qty":3},{"price":9.99,"qty":5}]
"""
print("baseline:", timeit.timeit("compute_total(items)", setup=SETUP, number=20000))
print("SAVE10 :", timeit.timeit("compute_total(items,'SAVE10')", setup=SETUP, number=20000))
print("WELCOME20:", timeit.timeit("compute_total(items,'WELCOME20')", setup=SETUP, number=20000))
