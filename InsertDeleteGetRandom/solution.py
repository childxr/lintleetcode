import random

class RandomizedSet:
    
    def __init__(self):
        # do intialization if necessary
        self.arr = []
        self.cnt = 0
        self.mapper = {}

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        # write your code here
        if self.mapper.has_key(val):
            return False
        self.arr.append(val)
        self.cnt += 1
        self.mapper[val] = self.cnt
        return True

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        # write your code here
        if self.mapper.has_key(val):
            loc = self.mapper[val]
            last_elem = self.arr[self.cnt-1]
            self.mapper[last_elem] = loc
            self.cnt -= 1
            del self.arr[-1]
            return True
        else:
            return False

    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        # write your code here
        n = random.randrange(self.cnt)
        return self.arr[n]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()
