"""

Test
====

.. autosummary::
    :toctree: stubs/
    :template: autosummary/class.rst

    Base
    Child
"""
class Base:
    """Parent class"""
    def __init__(self):
        self.attr = 0
        """Base class attribute"""

    @property
    def documented_attr(self):
        """Attribute that gets documented"""
        return self.attr

    @documented_attr.setter
    def documented_attr(self, value):
        self.attr = value


class Child(Base):
    """Child class"""
    def print_attr(self):
        """Print attr value"""
        print(self.attr)
