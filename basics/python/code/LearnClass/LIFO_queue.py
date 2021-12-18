class LIFO_queue:
    def __init__(self):
        self.stackCan = []
        print("setting up the constructor")

    def addValue(self, element):
        self.stackCan.append(element)

    def popValue(self):
        self.stackCan.pop()

    def isEmpty(self):
        return not len(self.stackCan)

    def peek(self):
        print(self.stackCan[-1])


if __name__ == "__main__":
    chips = LIFO_queue()
    chips.addValue(7)
    chips.addValue(8)
    chips.addValue(10)
    chips.peek()
    chips.popValue()
    chips.peek()
    chips.popValue()
    print("Is the stack empty: {}".format(chips.isEmpty()))
    chips.popValue()
    print("Now, is the stack empty: {}".format(chips.isEmpty()))
