#一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator(生成器)
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'