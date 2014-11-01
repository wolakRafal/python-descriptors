__author__ = 'RafalW'
__doc__ = "https://docs.python.org/2/howto/descriptor.html#id9"

# STATIC METHODS
# Since staticmethods return the underlying function with no changes, the example calls are unexciting
class E(object):
    def f(x):
        print x
    f = staticmethod(f)

print E.f(3)
print E().f(3)

# Class methods prepend the class reference to the argument list before calling the function.
# This format is the same for whether the caller is an object or a class:

class E(object):
    def f(klass, x):
        return klass.__name__, x
    f = classmethod(f)

print E.f(3)
print E().f(3)
# >> ('E', 3)
# >> ('E', 3)
