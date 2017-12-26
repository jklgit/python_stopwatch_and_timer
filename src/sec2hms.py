from metricprefix import metricprefix


def sec2hms(s, seconds=False, milliseconds=False):
    """
    Converts seconds into hms format.
    :param s: Seconds
    :param seconds: Always display seconds, even if 0? (False)
    :param milliseconds: Display milliseconds if seconds is displayed? (False)
    :return: String in hms format
    """
    (a, M, d, h, m, s) = sec2hms_vec(s, milliseconds=milliseconds)

    (m_s, s) = metricprefix(s)[1:3]

    if seconds:
        if a > 0:
            hms = '%d a %d M %d d %d h %d m %.4g %ss' % (a, M, d, h, m, s, m_s)
        elif M > 0:
            hms = '%d M %d d %d h %d m %.4g %ss' % (M, d, h, m, s, m_s)
        elif d > 0:
            hms = '%d d %d h %d m %.4g %ss' % (d, h, m, s, m_s)
        elif h > 0:
            hms = '%d h %d m %.4g %ss' % (h, m, s, m_s)
        elif m > 0:
            hms = '%d m %.4g %ss' % (m, s, m_s)
        else:
            hms = '%.4g %ss' % (s, m_s)
    else:
        if a > 100:
            (p, m_a, a) = metricprefix(a)
            hms = '%.4g %sa' % (a, m_a)
        elif a > 0:
            hms = '%d a %d M' % (a, M)
        elif M > 0:
            hms = '%d M %d d' % (M, d)
        elif d > 0:
            hms = '%d d %d h' % (d, h)
        elif h > 0:
            hms = '%d h %d m' % (h, m)
        elif m > 0:
            hms = '%d m %.4g %ss' % (m, s, m_s)
        else:
            hms = '%.4g %ss' % (s, m_s)

    return hms


def sec2hms_vec(s, milliseconds=False):
    """
    Converts seconds into hms format.
    :param s: Seconds
    :param milliseconds: Display milliseconds?
    :return: (years, months, days, hours, minutes, seconds)
    """
    (a, s) = divmod(s, 365 * 24 * 3600)
    (M, s) = divmod(s, 365 * 24 * 3600 / 12)
    (d, s) = divmod(s, 24 * 3600)
    (h, s) = divmod(s, 3600)
    (m, s) = divmod(s, 60)

    if ((a > 0) | (M > 0) | (d > 0) | (h > 0) | (m > 0)) and not milliseconds:
        s = round(s)
        if s == 60:
            s = 0
            m = m + 1
            if m == 60:
                m = 0
                h = h + 1
                if h == 24:
                    h = 0
                    d = d + 1

    return a, M, d, h, m, s


def print_demo(s):
    print(str(s) + ' = ' + sec2hms(s))


if __name__ == '__main__':
    print_demo(2628000.1)
    print_demo(1e-9)
    print_demo(52e-3)
    print_demo(69)
    print_demo(1e4)
    print_demo(1e6)
    print_demo(1e9)
    print_demo(1e13)
