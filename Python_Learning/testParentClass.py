#coding=gbk
class ren:                          #父类1
    name = 'ren'                    
    def sayHello (self):
        print 'Hello World!!'
        
class dongwu:                       #父类2
    name = 'dongwu'
    def cry (self):
        print 'cry!!'
        
    
class chinaren(ren, dongwu):        #多重继承
    def sayHi (self):
        print 'hi, World!!'
        
if __name__ == '__main__':
    cr = chinaren()
    cr.sayHello()
    cr.sayHi()
    cr.cry()
    print cr.name
    pass
