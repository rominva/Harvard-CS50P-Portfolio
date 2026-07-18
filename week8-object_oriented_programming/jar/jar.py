class Jar:
    # initialize a cookie jar with the given capacity
    # capacity, which represents the maximum number of cookies
    def __init__(self, capacity=12):
        if type(capacity) is not int:
            raise ValueError
        if capacity < 0:
            raise ValueError
        
        # _ cause we don't have a setter
        self._capacity = capacity
        self._cookies = 0


    def __str__(self):
        return self.size * "🍪"


    # add cookies
    def deposit(self, n):
        if self._cookies + n > self._capacity:
            raise ValueError
        self._cookies += n


    def withdraw(self, n):
        if self._cookies - n < 0:
            raise ValueError
        self._cookies -= n


    # Just getter => read-only
    @property
    def capacity(self):
        return self._capacity
    

    # Shows the number of cookies
    # Just getter => read-only 
    # cause we change the size by withdraw() and deposit() not the size
    @property
    def size(self):
        return self._cookies
