#-*-coding:utf-8-*-
def filterKeyWordAndSave (sF, dF, kW):   
    f1 = open(sF, "r")
    f2 = open(dF, "w")
    alllines=f1.readlines();
    s = set()
    l = []
    for eachline in alllines:
        if kW in eachline:
            if '"' in eachline:
                str = eachline.split('"')[1]
                if str not in s:
                    s.add(str)
                    l.append(str)
                    f2.write(eachline.split('"')[1]+'\n')
    del s
    f1.close()
    f2.close()
    return l

sourceFile = "C:\\Users\\raychang\\Desktop\\rsync-to-svnbak.log"
destFile = "C:\\Users\\raychang\\Desktop\\rsync-to-svnbak1.log"
keyWord = 'No such device'

l1 = []
l1 = filterKeyWordAndSave(sourceFile, destFile, keyWord)
print l1