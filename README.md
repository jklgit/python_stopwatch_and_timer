# Python Stopwatch and Timer

This is a little project, where I try to figure out how datatypes behave in Python and how some basic functions work.

## stopwatch.py

This is a stop watch, which runs in console. Once executed, type `Enter` to hold the time. Type `0` and then `Enter` to reset the timer. E.g.:

```
15:13:12.806  |  0 s  |  0 s
15:13:16.563  |  3.757 s  |  3.757 s
15:13:20.090  |  7.284 s  |  3.527 s
15:13:23.668  |  10.86 s  |  3.578 s
15:13:24.435  |  11.63 s  |  766 ms
15:13:25.068  |  12.26 s  |  633 ms
15:13:25.219  |  12.41 s  |  151 ms0
15:13:29.061  |  0 s  |  3.842 s
15:13:31.299  |  2.238 s  |  2.238 s
15:13:33.003  |  3.942 s  |  1.704 s
```
The first column is the OS time in 24 hour format. The second column displays the time since last reset. The third column displays the time past since last stop.

## timer.py

This is a timer, which also runs in console. It is only compatible with Microsoft Windows since it is using `winsound` to play an alarm, once the timer reaches zero. The program will ask for a user input, where a timespan can be chosen. E.g.:

```
How many seconds (default: 10 m 0 s)? 5h 15m 120s
5 h 17 m 0 s
5 h 16 m 59 s
5 h 16 m 58 s
5 h 16 m 57 s
5 h 16 m 56 s
...
```
The input can be given in seconds or a time in hms-format. For example, following inputs are allowed:

* `13`, ` 13   s ` or `13 secs`
* `1e10 hours`
* `1 kyear` (equals to 1000 years)

## timer_with_repeat.py

Same timer as in `timer.py`, but this one will repeat itself after reaching zero. Every time it reaches zero, it will play sound for a few seconds.
