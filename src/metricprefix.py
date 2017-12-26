from math import log10, floor, ceil, fmod, isinf, isnan


def metricprefix(v, n_root=1, b_numprefix=0):

    if isinstance(v, (list, tuple)):
        v_max = max(map(abs, v))
    elif isinstance(v, (float, int)):
        v_max = abs(v)
    else:
        print('Wrong data type!')

    # Handle 0, inf and nan
    if (v_max == 0) | isinf(v_max) | isnan(v_max):
        return 0, '', v

    p = log10(v_max**(1/n_root))/3

    if p < 0:
        if fmod(p, 1) != 0:
            p = ceil(p) - 1
    else:
        p = floor(p)

    p = 3*p

    if b_numprefix:
        if p == 0:
            m = ''
        else:
            m = '10^%d' % p

    else:
        m = switch_p(p)

    if n_root > 1:
        ''
    else:
        p_root = 0

    p = p*n_root + p_root

    if isinstance(v, (float, int)):
        v = v/10**p
    else:
        v = [x/10**p for x in v]

    return p, m, v


def switch_p(p):
    return {
        0: '',
        3: 'k',
        6: 'M',
        9: 'G',
        12: 'T',
        15: 'P',
        18: 'E',
        21: 'Z',
        24: 'Y',
        -3: 'm',
        -6: 'µ',
        -9: 'n',
        -12: 'p',
        -15: 'f',
        -18: 'a',
        -21: 'z',
        -24: 'y'
    }.get(p, '10^%d' % p)


def print_demo(v):
    (p, m, v_new) = metricprefix(v)
    m_mult = ''
    if m != '':
        if m[0] == '1':
            m_mult = '*'

    if isinstance(v, (float, int)):
        print('%.4g = %.4g%s%s' % (v, v_new, m_mult, m))
    else:
        def list_to_str(x):
            return '[%s]' % ', '.join(map(lambda y: '%.4g' % y, x))
        print('%s = %s%s%s' % (list_to_str(v), list_to_str(v_new), m_mult, m))

if __name__ == '__main__':
    # main will generate the following output:
    # 1e-09 = 1n
    # -1.21e-05 = -12.1µ
    # 0.01 = 10m
    # 1.234e+06 = 1.234M
    # 1.2e+37 = 12*10^36
    # [-0.0001235, 2e-05] = [-123.5, 20]µ
    # 0 = 0
    # -inf = -inf
    # nan = nan
    print_demo(1e-9)
    print_demo(-12.1e-6)
    print_demo(1e-2)
    print_demo(12.345e5)
    print_demo(12e36)
    print_demo([x*1e-4 for x in [-1.235, 0.2]])
    print_demo(0)
    print_demo(float('-inf'))
    print_demo(float('nan'))
