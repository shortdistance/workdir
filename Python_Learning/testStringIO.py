import cStringIO

output = cStringIO.StringIO()
print cStringIO.InputType
print cStringIO.OutputType

output.write('First line.\n')
print >>output, 'Second line.'

contents = output.getvalue()
print contents
output.close()