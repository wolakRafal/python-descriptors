__author__ = 'RafalW'

__doc__ = "https://docs.python.org/2/howto/descriptor.html#functions-and-methods"

class D(object):
    def f(self, x):
        return x

d = D()
print D.__dict__['f'] # Stored internally as a function

print D.f             # Get from a class becomes an unbound method
print d.f             # Get from an instance becomes a bound method