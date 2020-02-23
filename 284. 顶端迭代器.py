# Below is the interface for Iterator, which is already defined for you.
#
class Iterator:

    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """





    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator

        self.peek_num = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peek_num is None:
            self.peek_num = self.iterator.next()
        return self.peek_num


    def next(self):
        """
        :rtype: int
        """
        if self.peek_num is not None:
            num = self.peek_num
            if self.iterator.hasNext():
                self.peek_num = self.iterator.next()
            else:
                self.peek_num = None
            return num
        else:
            return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """

        if self.peek_num is not None or self.iterator.hasNext():
            return True
        else:
            return False

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].