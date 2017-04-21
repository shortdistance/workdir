#-*- coding:utf-8 -*-
def byLineReader(filename) :
    f = open(filename)
    line = f.readline()
    while line :
        yield line
        line = f.readline()
    f.close()
    yield None

def processLine(line):
    print line

def FileOperator(infile):
    reader = byLineReader(infile)
    line = reader.next()
    processLine(line)
    while line:
        line = reader.next()
        if line:
            processLine(line)
            

if __name__ == '__main__':
    FileOperator('./file1.txt')