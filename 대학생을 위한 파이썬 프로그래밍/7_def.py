def count(number):
    n=1
    while n <= number:
        print(n)
        n += 1

def times_tables(num):
    n=1
    while n <= 10:
        print(n, "x", num, "=", n*num)
        n += 1

count(5)
times_tables(10)
