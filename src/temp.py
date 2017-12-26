def select(t, *index): return tuple(n for (i, n) in enumerate(t) if i in index)

t = ('0', '1', '2', '3')
select(t, 1, 3)

