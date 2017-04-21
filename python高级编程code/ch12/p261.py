#!/usr/bin/python
# page 261

import profiler 
import random
eat_it = profiler.profile('you bad boy!')(eat_memory)
please = eat_it()
print profiler.stats
