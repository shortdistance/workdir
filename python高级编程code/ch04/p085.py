_observers = []
def add_observer(observer):
    _observers.append(observer)

def get_observers():
    """Makes sure _observers cannot be modified."""
    return tuple(_observers)

class Citizen(object):
    def __init__(self):
        self._message = 'Go boys'
    def _get_message(self):
        return self._message
    kane = property(_get_message)

print Citizen().kane
