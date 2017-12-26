import time
import winsound
from sec2hms import sec2hms
from hms2sec import hms2sec

secs = 10*60

secs_in = input('How many seconds (default: ' + sec2hms(secs) + ')? ')

if secs_in != '':
    secs = hms2sec(secs_in)

while secs > 0:
    print(sec2hms(secs, seconds=True))
    time.sleep(1)
    secs = secs - 1

print('Done!')

while 1:
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
