__author__ = 'RafalW'

class RevealAccess(object):
    """A data descriptor that sets and returns values
       normally and prints a message logging their access.
    """

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print 'Retrieving', self.name
        return self.val

    def __set__(self, obj, val):
        print 'Updating', self.name
        self.val = val


class MyClass(object):
    x = RevealAccess(10, 'x')
    y = RevealAccess(50, 'y')

m = MyClass()
print m.x
print m.y
