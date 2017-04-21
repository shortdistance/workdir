from doctest import IGNORE_EXCEPTION_DETAIL
from doctest import REPORT_ONLY_FIRST_FAILURE

import os
try:
    os._exit(0)
except os.EX_SOFTWARE:
    print 'internal softwar error'
    raise

import doctest
TEST_OPTIONS = (doctest.ELLIPSIS |
                doctest.NORMALIZE_WHITESPACE | 
                doctest.REPORT_ONLY_FIRST_FAILURE)

print TEST_OPTIONS
