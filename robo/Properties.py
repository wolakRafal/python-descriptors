__author__ = 'RafalW'

__doc__ = """ https://docs.python.org/2/howto/descriptor.html#id7 """

class C(object):
    def getx(self): return self.__x
    def setx(self, value): self.__x = value
    def delx(self): del self.__x
    x = property(getx, setx, delx, "I'm the 'x' property.")

# Example: For instance, a spreadsheet
# class may grant access to a cell value through Cell('b10').value.
# Subsequent improvements to the program require the cell to be recalculated on every access; however,
# the programmer does not want to affect existing client code accessing the attribute directly.
#
# The solution is to wrap access to the value attribute in a property data descriptor:

class Cell(object):
#    . . .
    def getvalue(self, obj):
        "Recalculate cell before returning value"
        self.recalc()
        return obj._value
    value = property(getvalue)