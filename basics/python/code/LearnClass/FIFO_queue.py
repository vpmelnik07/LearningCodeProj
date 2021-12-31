class FIFO_queue:
    def __init__(self):
        self.queue = []
        print("gearing up for FIFO queue control!")

    def addFIFO(self,element):
        self.queue.append(element)

    def popFIFO(self):
        self.queue.reverse()
        self.queue.pop()
        self.queue.reverse()

    def peekFIFO(self):
        self.queue.reverse()
        print(self.queue[-1])
        self.queue.reverse()

    def isEmpty(self):
        return not len(self.queue)

    def showFIFO(self):
        print(self.queue)

if __name__ == "__main__":
    FIFO = FIFO_queue()
    FIFO.addFIFO(4)
    print("Queue empty: ".format(FIFO.isEmpty()))
    FIFO.addFIFO(5)
    print("checking for the 1st element: {}".format(FIFO.peekFIFO()))
    print("show me all of the stack: {}".format(FIFO.showFIFO()))
    FIFO.addFIFO(10)
    print("show me all of the stack: {}".format(FIFO.showFIFO()))
    FIFO.popFIFO()
    FIFO.popFIFO()
    print("Queue empty: ".format(FIFO.isEmpty()))
    FIFO.popFIFO()
