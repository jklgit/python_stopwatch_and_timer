class AnyType(object):
    def __init__(self, val):
        self.v = val
        self.was_tuple = isinstance(val, tuple)

    def __abs__(self):
        self.v = fun_operation(self.v, abs)
        return self

    def __add__(self, other):
        self.v = math_operation(self.v, other, lambda x, y: x + y)
        return self

    def __mul__(self, other):
        self.v = math_operation(self.v, other, lambda x, y: x * y)
        return self

    def __truediv__(self, other):
        self.v = math_operation(self.v, other, lambda x, y: x / y)
        return self

    def __floordiv__(self, other):
        self.v = math_operation(self.v, other, lambda x, y: x // y)
        return self

    def __pow__(self, other):
        self.v = math_operation(self.v, other, pow)
        return self

    def __str__(self):
        return str(self.v)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if isinstance(self.v, (list, tuple)):
            try:
                result = self.v[self.index]
            except IndexError:
                raise StopIteration
            self.index += 1
            return result
        elif isinstance(self.v, (float, int)):
            if self.index == 0:
                self.index += 1
                return self.v
            else:
                raise StopIteration

        else:
            print('Not defined!')

    def max(self):
        t = type(self.v).__name__
        if isinstance(self.v, (list, tuple)):
            return max(self.v)
        elif isinstance(self.v, (float, int)):
            return self.v
        else:
            print('Not defined!')

    def get_data(self):
        if self.was_tuple:
            return tuple(self.v)
        else:
            return self.v


def fun_operation(a, op_fun):
    if isinstance(a, (list, tuple)):
        a = list(map(op_fun, a))
    elif isinstance(a, (float, int)):
        a = op_fun(a)
    else:
        print('Not defined!')
    return a


def math_operation(a, b, op_fun):
    if isinstance(b, AnyType):
        b = b.v
    if isinstance(a, (list, tuple)):
        if isinstance(b, (list, tuple)):
            a = [op_fun(x, y) for x, y in zip(a, b)]
        elif isinstance(b, (float, int)):
            a = [op_fun(x, b) for x in a]
        else:
            print('Not defined!')
    elif isinstance(a, (float, int)):
        if isinstance(b, (list, tuple)):
            a = [op_fun(x, a) for x in b]
        elif isinstance(b, (float, int)):
            a = op_fun(a, b)
        else:
            print('Not defined!')
    else:
        print('Not defined!')
    return a


if __name__ == '__main__':
    print('Demo:')
    v = AnyType((1, 2, 3))
    v = v**AnyType([4, 5, 6])
    v = v**[1, 2, 0]
    v = v**5.1 + 1
    print(v.max())
    # prints (2.0, 2251799813685243.5, 2.0)
