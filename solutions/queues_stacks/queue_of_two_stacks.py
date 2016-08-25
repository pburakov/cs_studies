class Queue:
    def __init__(self):
        """
        Implementation of a Queue using two stacks.

        Implementation details:
        Let stack 1 serve as a main storage
        Let stack 2 be used as an aux storage to rearrange items on dequeue
        To keep aux stack from redundant rearrangement, store a flag that it's safe to use it
        Stacks are implemented using Python lists (to save coding time). append() and pop() operations are O(1)
        """
        self.main = []
        self.aux = []
        self.use_aux = False

    def enqueue(self, x):
        if self.use_aux is True:
            n = len(self.aux)
            self.main.clear()
            for i in range(n - 1, -1, -1):  # rearranging in reverse order
                self.main.append(self.aux[i])
        self.main.append(x)
        self.use_aux = False

    def dequeue(self):
        n = len(self.main)
        if self.use_aux is False:
            self.aux.clear()
            for i in range(n - 1, -1, -1):  # adding in reverse order
                self.aux.append(self.main[i])
        # now it's safe to use aux for the next operation unless enqueue() is invoked
        self.use_aux = True
        x = self.aux.pop()
        return x
