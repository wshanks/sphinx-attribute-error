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


class Child(Base):
    """Child class"""
    def print_attr(self):
        """Print attr value"""
        print(self.attr)
