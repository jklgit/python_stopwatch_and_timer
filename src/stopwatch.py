import datetime
from hms import sec2hms

a = ''
t = datetime.datetime.now()
t_old = t
t_0 = t
while a == '':
    t_current = t.strftime('%H:%M:%S.%f')[:-3]
    dt_0 = sec2hms((t - t_0).total_seconds())
    dt = sec2hms((t - t_old).total_seconds())
    a = input('%s  |  %s  |  %s' % (t_current, dt_0, dt))
    t_old = t
    t = datetime.datetime.now()
    if a == '0':
        t_0 = t
        a = ''

