def fibonacci():
    a, b = 0, 1

    while True:
        c = a + b
        yield c
        a, b = b, c


def main():
    fib = fibonacci()

    for n in range(0, 10):
        print(next(fib))


if __name__ == '__main__':
    main()
