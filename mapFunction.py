#map() = applies a function to every item in an iterable (list, tuple, etc.)

#map(function, iterable)

store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

toEuros = lambda data: (data[0].upper(), data[1]*0.82)
storeEuros = list(map(toEuros, store))

toDollars = lambda data: (data[0].upper(), int(data[1]/0.82))
storeDollars = list(map(toDollars, store))

for i in storeEuros:
    print(i)
print()
for i in storeDollars:
    print(i)