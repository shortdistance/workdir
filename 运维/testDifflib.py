import difflib

text1 = '''
hello world
hello world1
hello world2
'''
text1_lines = text1.splitlines()

text2 = '''
hello world
hello world0
hello hadoop2
'''

text2_line2 = text2.splitlines()

#d = difflib.Differ()
#diff = d.compare(text1_lines, text2_line2)
#print list(diff)

d = difflib.HtmlDiff()
print d.make_file(text1_lines, text2_line2)