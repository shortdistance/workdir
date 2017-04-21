#!/usr/bin/python
# page 251

import tempfile, os, cProfile, pstats
def profile(column='time', list=5):
    def _profile(function):
        def __profile(*args, **kw):
            s = tempfile.mktemp()
            profiler = cProfile.Profile()
            profiler.runcall(function, *args, **kw)
            profiler.dump_stats(s)
            p = pstats.Stats(s)
            p.sort_stats(column).print_stats(list)
        return __profile
    return _profile

from myapp import main
@profile('time', 6)
def main_profiled():
    return main()

main_profiled()
