# -*-coding:utf-8 -*-
"""
#简单工厂模式
#应用计算器
#模式特点：工厂根据条件产生不同功能的类。
#程序实例：四则运算计算器，根据用户的输入产生相应的运算类，用这个运算类处理具体的运算。
#代码特点：C/C++中的switch...case...分支使用字典的方式代替。
#
#　　　　　使用异常机制对除数为0的情况进行处理。
"""

#运算类
class Operation:
    def GetResult(self):
        pass

#加法运算类
class OperationAdd(Operation):
    def GetResult(self):
        return self.op1 + self.op2

#减法运算类
class OperationSub(Operation):
    def GetResult(self):
        return self.op1 - self.op2

#乘法运算类
class OperationMul(Operation):
    def GetResult(self):
        return self.op1 * self.op2

#除法运算类
class OperationDiv(Operation):
    def GetResult(self):
        try:
            result = self.op1 / self.op2
            return result
        except:
            print "error:divided by zero."
            return 0

#未知运算类
class OperationUndef(Operation):
    def GetResult(self):
        print "Undefine operation."
        return 0

#运算累工厂
class OperationFactory:
    #运算累汇总
    operation = {}
    operation["+"] = OperationAdd();
    operation["-"] = OperationSub();
    operation["*"] = OperationMul();
    operation["/"] = OperationDiv();

    #创建一个运算类
    def createOperation(self, ch):
        if ch in self.operation:
            op = self.operation[ch]
        else:
            op = OperationUndef()
        return op


if __name__ == "__main__":
    op = raw_input("operator: ")
    opa = input("a: ")
    opb = input("b: ")
    factory = OperationFactory()
    cal = factory.createOperation(op)
    cal.op1 = opa
    cal.op2 = opb
    print cal.GetResult()
