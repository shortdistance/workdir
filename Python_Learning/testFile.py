#coding=utf8

if __name__ == '__main__':
    l = [];
    l = ['hello world\n', 'i love you\n', 'my god!!']
    f1 = open('c:/1.txt','a')
    f1.writelines(l)
    
    f1.close()
    pass