# -*- coding:gbk -*- 
'''ʾ��2: �滻����(װ��) 
װ�κ����Ĳ����Ǳ�װ�εĺ������󣬷���ԭ�������� 
װ�ε�ʵ�����: myfunc = deco(myfunc)'''
  
def deco(func): 
    print("before myfunc() called.") 
    func() 
    print("after myfunc() called.") 
    return func 
  
def myfunc(): 
    print(" myfunc() called.") 
  
myfunc = deco(myfunc) 
  
myfunc() 
myfunc() 
