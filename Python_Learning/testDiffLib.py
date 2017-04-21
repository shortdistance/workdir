#coding=utf8
import difflib

ctrl=u"abcdefghijklmn"
attr=u"abcdefghijklmn,"
import difflib
'''
matcher=difflib.SequenceMatcher()
#matcher.set_seqs(ctrl,attr)
matcher.set_seq1(ctrl)
matcher.set_seq2(attr)
print matcher.ratio()
'''
matcher=difflib.SequenceMatcher(None, ctrl, attr)
print matcher.ratio()
print matcher.real_quick_ratio()

print matcher.get_opcodes()