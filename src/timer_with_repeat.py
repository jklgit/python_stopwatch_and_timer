import time
import winsound
import threading
import datetime
from sec2hms import sec2hms
from hms2sec import hms2sec


class PlayMusicThread(threading.Thread):
    def __init__(self, s):
        threading.Thread.__init__(self)
        self.total_seconds = min([s, 5])

    def run(self):
        total_seconds = 0
        dt = 0
        while (total_seconds + 2*dt) <= self.total_seconds:
            total_seconds += dt
            t = datetime.datetime.now()
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            dt = (datetime.datetime.now() - t).total_seconds()


secs_0 = 10*60

secs_in = input('How many seconds (default: ' + sec2hms(secs_0) + ', min: 1 s)? ')
if secs_in != '':
    secs_0 = max([hms2sec(secs_in), 1])

secs = secs_0

while 1:
    print(sec2hms(secs, seconds=True))
    time.sleep(1)
    secs = secs - 1

    if secs <= 0:
        secs = secs_0
        PlayMusicThread(secs_0).start()
