#codeing:utf-8

class Car:
    def __init__ (self, PingPai='Mini', Color='Yellow'):
        self.PingPai=PingPai
        self.Color=Color
        
    def getPingPai (self):
        return self.PingPai

    def getColor (self):
        return self.Color

c = Car('Dos Aut', 'White')
print c.getPingPai()
print c.getColor()
        
        