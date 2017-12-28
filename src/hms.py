import re
from metricprefix import metricprefix


def hms2sec(hms):
    digit = r'([+-]?\d+(.\d+)?(e[+-]?\d+)?)'
    m = re.match(r'^\s*' + digit + r'\s*$', hms)
    if m:
        return float(hms)
    else:
        prefix = {
            'yocto': 1e-24,
            'zotto': 1e-21,
            'atto': 1e-18,
            'femto': 1e-15,
            'pico': 1e-12,
            'nano': 1e-9,
            'micro': 1e-6,
            'milli': 1e-3,
            'kilo': 1e3,
            'Mega': 1e6,
            'Giga': 1e9,
            'Tera': 1e12,
            'Peta': 1e15,
            'Exa': 1e18,
            'Zetta': 1e21,
            'Yotta': 1e24
        }

        # Generate first letter and lowercase keys
        for key in list(prefix):
            value = prefix[key]
            prefix[key.lower()] = value
            prefix[key[0:1].lower()] = value

        p = r'(' + '|'.join([key for key in prefix]) + ')?'

        m = re.match(r'^(\s*' +
                     digit + '\s*' + p + '(a|yr|yrs|year|years))?(\s*' +
                     digit + '\s*' + p + '(M|mon|mons|month|months))?(\s*' +
                     digit + '\s*' + p + '(d|ds|day|days))?(\s*' +
                     digit + '\s*' + p + '(h|hs|hr|hrs|hour|hours))?(\s*' +
                     digit + '\s*' + p + '(m|min|mins|minute|minutes))?(\s*' +
                     digit + '\s*' + p + '(s|sec|secs|second|seconds))?$', hms)
        if m:
            hms = m.groups()[1:32:6]
            p = m.groups()[4:37:6]

            hms = [float(x) if x is not None else 0 for x in hms]
            p = [prefix[x] if x is not None else 1 for x in p]

            hms[0] = hms[0]*p[0] * 3600 * 24 * 365
            hms[1] = hms[1]*p[1] * 3600 * 24 * 365/12
            hms[2] = hms[2]*p[2] * 3600 * 24
            hms[3] = hms[3]*p[3] * 3600
            hms[4] = hms[4]*p[4] * 60
            hms[5] = hms[5]*p[5]

            return sum(hms)

        else:
            return None


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


def print_demo(a):
    print('%s = %d sec = %s' % (a, hms2sec(a), sec2hms(hms2sec(a))))


def main():
    print('Demo-Inputs:')
    print_demo('1200')
    print_demo('4 hours 5 minutes 60 seconds')
    print_demo('1.3 Gigaseconds')
    print_demo('1 millimonths 5 mins')
    print()
    while True:
        a = input('Enter an hms expression: ')
        print_demo(a)


if __name__ == '__main__':
    main()
