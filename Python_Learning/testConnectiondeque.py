#-*-coding:utf-8-*-
if __name__ == '__main__':
    from collections import deque
    d = deque('abcd')
    d.append('d')
    print d
    
    d.remove('d')
    print d

    d.pop()     #�����ȳ�
    print d

    d.popleft() #�����ȳ�
    print d
    

    d1  = deque("hello world")
    d1.reverse()  #��ת
    print d1
    
    d1.rotate(-5)
    print d1
    print deque(open('D:\\12345.txt'), 5)
    pass

