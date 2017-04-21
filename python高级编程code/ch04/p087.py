class Base(object):
    def __secret(self):
        print "don't tell"
    def public(self):
        self.__secret()

#Base.__secret
print dir(Base)

class Derived(Base):
    def __secret(self):
        print "never ever"

Derived().public()
