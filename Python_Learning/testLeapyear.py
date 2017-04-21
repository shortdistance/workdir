#-*-coding:utf-8-*-

def isLeapYear (year):
    if year%4==0 and year % 100 !=0:
        return True
    elif year % 400 ==0:
        return True
    else:
        return False
    
    
if __name__ == '__main__':
    print isLeapYear(1992)
    print isLeapYear(1996)
    print isLeapYear(2000)
    print isLeapYear(1967)
    print isLeapYear(1900)
    print isLeapYear(1600)