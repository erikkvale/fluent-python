"""
This is the class implementation of the strategy design pattern
-Context
-Strategy (interface)
-Concrete strategies

"""

from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:
    """
    Context
    """
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):
    """
    Strategy (Abstract base class)
    """
    @abstractmethod
    def discount(self, order):
        """Return discount as a positive dollar amount"""


class FidelityPromo(Promotion):
    """
    Concrete strategy 1:
    5% discount for customers with 1000 or more fidelity points
    """
    def discount(self, order):
        if order.customer.fidelity >= 1000:
            return order.total() * 0.05
        else:
            return 0


class BulkItemPromo(Promotion):
    """
    Concrete strategy 2:
    10% discount for each LineItem with 20 or more points
    """
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount


class LargeOrderPromo(Promotion):
    """
    Concrete strategy 3:
    7% discount for orders with 10 or more distinct items
    """
    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            discount = order.total() * 0.07
        return 0


if __name__=='__main__':
    import doctest
    doctest.testmod()