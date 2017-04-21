#-*-coding:utf-8-*-
if __name__ == '__main__':
    from collections import deque
    d = deque('abcd')
    d.append('d')
    print d
    
    d.remove('d')
    print d

    d.pop()     #后入先出
    print d

    d.popleft() #先入先出
    print d
    

    d1  = deque("hello world")
    d1.reverse()  #反转
    print d1
    
    d1.rotate(-5)
    print d1
    print deque(open('D:\\12345.txt'), 5)
    pass

