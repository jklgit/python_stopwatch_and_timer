import re


def hms2sec(hms):
    digit = r'([+-]?\d+(.\d+)?(e[+-]?\d+)?)'
    m = re.match(r'^\s*' + digit + r'\s*$', hms)
    if m:
        return float(hms)
    else:
        prefix = {
            'y': 1e-24,
            'z': 1e-21,
            'a': 1e-18,
            'f': 1e-15,
            'p': 1e-12,
            'n': 1e-9,
            'µ': 1e-6,
            'm': 1e-3,
            'k': 1e3,
            'M': 1e6,
            'G': 1e9,
            'T': 1e12,
            'P': 1e15,
            'E': 1e18,
            'Z': 1e21,
            'Y': 1e24,
            'yocto': 1e-24,
            'zotto': 1e-21,
            'atto': 1e-18,
            'femto': 1e-15,
            'pico': 1e-12,
            'nano': 1e-9,
            'micro': 1e-6,
            'milli': 1e-3,
            'kilo': 1e3,
            'mega': 1e6,
            'giga': 1e9,
            'tera': 1e12,
            'peta': 1e15,
            'exa': 1e18,
            'zetta': 1e21,
            'yotta': 1e24
        }
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


if __name__ == '__main__':
    print(hms2sec('1mM'))
    print(hms2sec(' 1e-3km 10ms'))
