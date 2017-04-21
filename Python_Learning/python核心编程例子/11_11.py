#-------------------------------------------------------------------------------
# Name:        Ä£¿é2
# Purpose:
#
# Author:      raychang
#
# Created:     22/09/2014
# Copyright:   (c) raychang 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import __future__

def map1(seq1, seq2):
    if isinstance(seq1, list) and isinstance(seq1, list) and len(seq1) == len(seq2):
        return map(lambda x,y:(x,y), seq1, seq2 )

if __name__ == '__main__':
    l1 = [1,2,3]
    l2 = ['1','haha','world']
    print map1(l1,l2)
