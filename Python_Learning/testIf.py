#-*-coding:utf-8-*-

def score (x):
    try:
        score = int(x)
    except Exception, e:
        return 'error info: ',e
    if  90<= score<=100:
        return 'A: 90每100'
    elif 80<= score<=89:
        return 'B: 80每89'
    elif 70<= score<=79:
        return 'C: 70每79'
    elif 60<= score<=69:
        return 'D: 60每69'
    elif score<60:
        return '<60'
    else:
        return 'score in valid!!'

print score(20)
print score(60)
print score(70)
print score(82)
print score(95)
print score(100)
print score(101)
print score('zhangleid')