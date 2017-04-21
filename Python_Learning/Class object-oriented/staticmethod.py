#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      raychang
#
# Created:     08/09/2014
# Copyright:   (c) raychang 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class test():
    def __init__(self, x,y):
        self.x = x
        self.y = y
    @staticmethod
    def getX():
        return 5

    @classmethod
    def getY(cls):
        print cls.__name__
def main():
    t = test.getX()
    print t

    print test.getY()
    pass

if __name__ == '__main__':
    main()
