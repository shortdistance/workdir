class FirstClass(object):
    def _get_price(self):
        return '$ 500'
    def _get_the_price(self):
        return self._get_price()
    price = property(_get_the_price)

class SecondClass(FirstClass):
    def _get_price(self):
        return '$ 20'

plane_ticket = SecondClass()
print plane_ticket.price
