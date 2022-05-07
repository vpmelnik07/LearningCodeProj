class List2Digit:
    def __init__(self):
        pass

    def joinListDig(self,list):
        num = ""
        for i in range(len(list)):
            num += str(list[i])
        return num

if __name__ == '__main__':
    list = [1,2,3]
    num = List2Digit()
    print(type(num.joinListDig(list)))
